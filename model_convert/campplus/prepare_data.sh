#!/bin/bash

data=data

download_dir=${data}/download_data
rawdata_dir=${data}/raw_data

./download_data.sh --download_dir ${download_dir}

if [ ! -d ${rawdata_dir}/3dspeaker ]; then
    mkdir -p ${rawdata_dir}/3dspeaker
    mkdir -p ${rawdata_dir}/3dspeaker/test
    tar -xzvf ${download_dir}/test.tar.gz -C ${rawdata_dir}/3dspeaker/
fi

echo "Decompress success !!!"