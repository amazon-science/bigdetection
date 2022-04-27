This directory provides partial configuration implemented by detectron2. Please follow the installation of [CenterNet2](https://github.com/xingyizhou/CenterNet2) to reproduce all results.

## Training

***Pre-training***

To pre-train a CenterNet2 with ResNet-50 backbone on BigDetection using 8 GPUs, run:
```
python projects/CenterNet2/train_net.py \
    --config-file projects/CenterNet2/configs/centernet2_R_50_BigDet_8x.yaml 
    --num-gpus 8
```

***Data efficiency***

To fine-tune a BigDetection pre-trained Faster R-CNN on partial COCO, run:
```
# 1% COCO
python projects/CenterNet2/train_net.py \
    --config-file projects/CenterNet2/configs/faster_rcnn_R_50_FPN_COCO-1.yaml 
    --num-gpus 8
    MODEL.WEIGHTS /path/to/bigdet_pretrained_rcnn_checkpoint

# 2% COCO
python projects/CenterNet2/train_net.py \
    --config-file projects/CenterNet2/configs/faster_rcnn_R_50_FPN_COCO-2.yaml 
    --num-gpus 8
    MODEL.WEIGHTS /path/to/bigdet_pretrained_rcnn_checkpoint

# 5% COCO
python projects/CenterNet2/train_net.py \
    --config-file projects/CenterNet2/configs/faster_rcnn_R_50_FPN_COCO-5.yaml 
    --num-gpus 8
    MODEL.WEIGHTS /path/to/bigdet_pretrained_rcnn_checkpoint

# 10% COCO
python projects/CenterNet2/train_net.py \
    --config-file projects/CenterNet2/configs/faster_rcnn_R_50_FPN_COCO-10.yaml 
    --num-gpus 8
    MODEL.WEIGHTS /path/to/bigdet_pretrained_rcnn_checkpoint
```
