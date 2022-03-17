# Model Zoo

## BigDetection Pretrained Models
| Method | mAP (bigdet val) | Links |
| --- | :---: | :---: |
| YOLOv3 | 9.7 | [model]()/[config](configs/BigDetection/yolov3/yolov3_d53_mstrain-608_8x_bigdet.py) |
| Deformable DETR | 13.1 | [model]()/[config](configs/BigDetection/deformable_detr/deformable_detr_r50_16x2_8x_bigdet.py) |
| Faster R-CNN (C4)\* | 18.9 | [model]() |
| Faster R-CNN (FPN)\* | 19.4 | [model]() |
| CenterNet2\* | 23.1 | [model]() |
| Cascade R-CNN\* | 24.1 | [model]() |
| CBNetV2 | - | [model]()/[config](configs/BigDetection/cbnetv2/htc_cbv2_swin_base_giou_4conv1f_adamw_bigdet.py) |

## COCO Finetuned Models
| Method | mAP (coco minival/test-dev) | Links |
| --- | :---: | :---: |
| YOLOv3 | 30.5/- | [model]()/[config](configs/BigDetection/yolov3/yolov3_d53_mstrain-608_8x_bigdet.py) |
| Deformable DETR | 39.9/- | [model]()/[config](configs/BigDetection/deformable_detr/deformable_detr_r50_16x2_8x_bigdet.py) |
| Faster R-CNN (C4)\* | 38.8/- | [model]() |
| Faster R-CNN (FPN)\* | 40.5/- | [model]() |
| CenterNet2\* | 45.3/- | [model]() |
| Cascade R-CNN\* | 45.1/- | [model]() |
| CBNetV2-Swin-Base | 59.1/59.5 | [model]()/[config](configs/BigDetection/cbnetv2/htc_cbv2_swin_base_giou_4conv1f_adamw_bigdet.py) |
| CBNetV2-Swin-Base (TTA) | 59.5/59.8 | [model]()/[config](configs/BigDetection/cbnetv2/htc_cbv2_swin_base_giou_4conv1f_adamw_bigdet.py) |

### Notes:

- The models following `*` are implemented on another detection codebase [Detectron2](https://github.com/facebookresearch/detectron2). Here we provide the pretrained checkpoints. The results can be reproduced following the installation of [CenterNet2](https://github.com/xingyizhou/CenterNet2) or [Detectron2](https://github.com/facebookresearch/detectron2).
- Most of pretrained models are trained for `8X` schedule on BigDetection.
- Pretrained models are finetuned for `1X` schedule on COCO.

## Data Efficiency
We followed [STAC](https://arxiv.org/abs/2005.04757) and [SoftTeacher](https://arxiv.org/abs/2106.09018) to evaluate on COCO data split for different partial annotation setting, and report the mAP performance. The results are shown in the following:

### 1% labeled data
| Method | mAP | Links |
| --- | :---: | :---: |
| Baseline | 9.8 | - |
| STAC | 14.0 | - |
| SoftTeacher | 20.5 | - |
| Ours | 25.3 | [model]() |

### 2% labeled data
| Method | mAP | Links |
| --- | :---: | :---: |
| Baseline | 14.3 | - |
| STAC | 18.3 | - |
| SoftTeacher | 26.5 | - |
| Ours | 28.1 | [model]() |

### 5% labeled data
| Method | mAP | Links |
| --- | :---: | :---: |
| Baseline | 21.2 | - |
| STAC | 24.4 | - |
| SoftTeacher | 30.7 | - |
| Ours | 31.9 | [model]() |

### 10% labeled data
| Method | mAP | Links |
| --- | :---: | :---: |
| Baseline | 26.2 | - |
| STAC | 28.6 | - |
| SoftTeacher | 34.0 | - |
| Ours | 34.1 | [model]() |
