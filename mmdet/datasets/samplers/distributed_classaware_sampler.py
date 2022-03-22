import math
import json

import numpy as np
import torch
from mmcv.runner import get_dist_info
from torch.utils.data import Sampler


class DistributedClassAwareSampler(Sampler):
    def __init__(self, dataset, samples_per_gpu=1, num_replicas=None, rank=None, seed=1, sample_weight_path=None):
        _rank, _num_replicas = get_dist_info()
        if num_replicas is None:
            num_replicas = _num_replicas
        if rank is None:
            rank = _rank
        self.dataset = dataset
        self.samples_per_gpu = samples_per_gpu
        self.num_replicas = num_replicas
        self.rank = rank
        self.epoch = 0
        self.seed = seed if seed is not None else 1

        assert hasattr(self.dataset, 'flag')
        assert len(self.dataset.flag) == len(self.dataset)
        self.num_samples = math.ceil(len(self.dataset) / self.num_replicas)

        with open(sample_weight_path, "r") as f:
            sample_weight = json.load(f)
        self.sample_weights = torch.tensor(
            list(sample_weight.values()), dtype=torch.float)

        self.indices = None
        self.set_epoch(-1)

    def __iter__(self):
        return iter(self.indices)

    def __len__(self):
        return self.num_samples        

    def set_epoch(self, epoch):
        self.epoch = epoch

        g = torch.Generator()
        g.manual_seed(self.seed + self.epoch)

        indices = torch.multinomial(
            self.sample_weights, len(self.dataset), generator=g, replacement=True
        ).numpy()

        self.flag = self.dataset.flag[indices]

        self.group_sizes = np.bincount(self.flag)
        self.num_samples = 0
        for i, j in enumerate(self.group_sizes):
            self.num_samples += math.ceil(self.group_sizes[i] / self.samples_per_gpu / 
                                          self.num_replicas) * self.samples_per_gpu
        self.total_size = self.num_samples * self.num_replicas

        indices_group = []
        for i, size in enumerate(self.group_sizes):
            if size > 0:
                flag_i_indice = np.where(self.flag == i)[0]
                assert len(flag_i_indice) == size

                indice = indices[flag_i_indice].tolist()
                extra = math.ceil(
                    size / self.samples_per_gpu / self.num_replicas
                ) * self.samples_per_gpu * self.num_replicas - len(indice)

                tmp = indice.copy()
                for _ in range(extra // size):
                    indice.extend(tmp)
                indice.extend(tmp[:extra % size])
                indices_group.extend(indice)

        assert len(indices_group) == self.total_size
        indices_group = [
            indices_group[j] for i in list(
                torch.randperm(
                    len(indices_group) // self.samples_per_gpu, generator=g))
            for j in range(i * self.samples_per_gpu, (i + 1) *
                           self.samples_per_gpu)
        ]

        offset = self.num_samples * self.rank
        indices_group = indices_group[offset:offset + self.num_samples]
        assert len(indices_group) == self.num_samples

        self.indices = indices_group


