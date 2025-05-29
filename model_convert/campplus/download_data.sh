#!/bin/bash

download_dir=data/download_data

[ ! -d ${download_dir} ] && mkdir -p ${download_dir}

if [ ! -f ${download_dir}/test.tar.gz ]; then
    echo "Downloading 3dspeaker test.tar.gz"
    wget --no-check-certificate https://speech-lab-share-data.oss-cn-shanghai.aliyuncs.com/3D-Speaker/test.tar.gz -P ${download_dir}
    md5=$(md5sum ${download_dir}/test.tar.gz | awk '{print $1}')
    [ $md5 != "45972606dd10d3f7c1c31f27acdfbed7" ] && echo "Wrong md5sum of 3dspeaker test.tar.gz" && exit 1
fi

echo "Download success !!!"

