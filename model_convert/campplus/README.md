# CAM++

## 准备数据

```
./prepare_data.sh
```

## 准备模型

```
onnxslim ../pretrained_models/CosyVoice-300M/campplus.onnx campplus_sim.onnx --input-shapes input:1,256,80 
```