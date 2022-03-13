#!/usr/bin/env bash

PORT=${PORT:-29500}

PYTHONPATH="$(dirname $0)/..":$PYTHONPATH \
python -m torch.distributed.launch \
    --nproc_per_node=8 --nnodes=5 --node_rank=0 --master_addr="172.31.0.27" --master_port=$PORT \
    $(dirname "$0")/train.py configs/cbnet/htc_cbv2_swin_base_bigdet_giou_4conv1f_400k.py --launcher pytorch \
    --cfg-options model.pretrained='./models/swin_base_patch4_window7_224_22k.pth'
