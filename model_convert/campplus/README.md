# CAM++

## 准备数据

```
./prepare_data.sh
```

## 准备模型

```
onnxslim ../pretrained_models/CosyVoice-300M/campplus.onnx campplus_sim.onnx --input-shapes input:1,256,80 
```

## 生成量化数据集

```
python generate_calib.py
```

## 编译axmodel

```
pulsar2 build --input campplus_sim.onnx --config config.json --output_dir campplus_axmodel --output_name campplus.axmodel
```