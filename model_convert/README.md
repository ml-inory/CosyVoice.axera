# CosyVoice模型转换

## 下载预编译模型

```
./download_pretrained_models.sh
```


## 安装Miniconda

参考 https://docs.conda.io/en/latest/miniconda.html


## 安装Python依赖

```
conda create -n cosyvoice -y python=3.10
conda activate cosyvoice
# pynini is required by WeTextProcessing, use conda to install it as it can be executed on all platform.
conda install -y -c conda-forge pynini==2.1.5
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com

# If you encounter sox compatibility issues
# ubuntu
sudo apt-get install sox libsox-dev
# centos
sudo yum install sox sox-devel
```