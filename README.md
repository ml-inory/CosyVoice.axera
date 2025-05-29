# CosyVoice.axera
FunAudioLLM CosyVoice on Axera platform


## 支持的平台

- [x] AX650N
- [ ] AX630C (Coming soon)


## 预编译模型下载

```
./download_models.sh
```

如需自行转换模型请参考[模型转换](/model_convert/README.md)


## AX650N运行

### 安装Miniconda

```
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh

source ~/miniconda3/bin/activate

conda init --all
```

### 安装依赖

#### OpenFST编译安装
```
# 安装编译依赖
sudo apt-get install -y build-essential autoconf libtool

# 下载并解压源码
wget http://www.openfst.org/twiki/pub/FST/FstDownload/openfst-1.8.2.tar.gz
tar -xzvf openfst-1.8.2.tar.gz
cd openfst-1.8.2

# 配置编译参数（启用grm扩展）
./configure --enable-grm --enable-static --enable-shared

# 编译安装（使用多核加速）
make -j$(nproc)
sudo make install

# 配置环境变量
echo 'export CPLUS_INCLUDE_PATH="/usr/local/include:$CPLUS_INCLUDE_PATH"' >> ~/.bashrc
echo 'export LIBRARY_PATH="/usr/local/lib:$LIBRARY_PATH"' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH="/usr/local/lib:$LD_LIBRARY_PATH"' >> ~/.bashrc
source ~/.bashrc

```

#### 安装SOX

```
sudo apt-get install -y sox libsox-dev
```


#### 创建虚拟环境

```
conda create -n cosyvoice -y python=3.10
conda activate cosyvoice
```

#### 安装Python依赖

```
pip install pynini==2.1.5
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com
```

