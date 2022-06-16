This is a bigdetection demo. 

##### Steps:

###### Replace 'bigdetection/mmdet/apis/inference.py' in original bigdetection program with new inference.py.

###### Checkpoint file download link:

[yolov3](https://download.openmmlab.com/mmdetection/v2.0/yolo/yolov3_d53_fp16_mstrain-608_273e_coco/yolov3_d53_fp16_mstrain-608_273e_coco_20210517_213542-4bc34944.pth)   -- Offered by mmdetection official contributor

[yolov3](https://big-detection.s3.us-west-2.amazonaws.com/bigdet_cpts/mmdetection_cpts/yolov3_d53_bigdet_8x.pth)   -- Offered by our bigdetection contributor

[detr](https://big-detection.s3.us-west-2.amazonaws.com/bigdet_cpts/mmdetection_cpts/deformable_detr_bigdet_8x.pth) -- Offered by our bigdetection contributor

[cbvnet](https://big-detection.s3.us-west-2.amazonaws.com/bigdet_cpts/mmdetection_cpts/htc_cbv2_swin_base_giou_4conv1f_bigdet.pth) -- Offered by our bigdetection contributor



###### Put the .checkpoint file in the checkpoints dictionary

——bigdetection——**checkpoints**——.checkpoint

​                              ——configs

​                             ——demo

​                              ——......



###### Run the following code in cmd terminal(using mmdetection official checkpoint file)

--Offered by mmdetection official contributor

```
python demo/image_demo.py demo/demo.jpg configs/BigDetection/yolov3/yolov3_d53_mstrain-608_1x_coco.py checkpoints/yolov3_d53_fp16_mstrain-608_273e_coco_20210517_213542-4bc34944.pth
```

-- Offered by our bigdetection contributor

```
python demo/image_demo.py demo/demo.jpg configs/BigDetection/yolov3/yolov3_d53_mstrain-608_8x_bigdet.py checkpoints/yolov3_d53_bigdet_8x.pth
```

```
python demo/image_demo.py demo/demo.jpg configs/BigDetection/deformable_detr/deformable_detr_r50_16x2_8x_bigdet.py checkpoints/deformable_detr_bigdet_8x.pth
```

```
python demo/image_demo.py demo/demo.jpg configs/BigDetection/cbnetv2/htc_cbv2_swin_base_giou_4conv1f_adamw_bigdet.py checkpoints/htc_cbv2_swin_base_giou_4conv1f_bigdet.pth
```

