import os, sys
import argparse
import glob
import numpy as np
import tqdm
import torchaudio.compliance.kaldi as kaldi
import tarfile
from utils import load_wav


def get_args():
    parser = argparse.ArgumentParser(description='Generate calibration dataset for quantization')
    parser.add_argument('--output_path', default='./calib_dataset')
    parser.add_argument('--input_path', default='./data/raw_data/3dspeaker/test')
    parser.add_argument('--max_num', type=int, default=10, help='Max calib data num')
    args = parser.parse_args()
    return args


def preprocess(speech):
    feat = kaldi.fbank(speech,
                        num_mel_bins=80,
                        dither=0,
                        sample_frequency=16000)
    feat = feat - feat.mean(dim=0, keepdim=True)
    return feat


def main():
    args = get_args()
    
    os.makedirs(args.output_path, exist_ok=True)

    sr = 16000
    seq_len = 256

    tf = tarfile.open('calib.tar.gz', 'w:gz')
    for wav_path in tqdm.tqdm(glob.glob(f'{args.input_path}/*/*.wav')[:args.max_num]):
        speech_16k = load_wav(wav_path, sr)
        feat = preprocess(speech_16k).numpy()
        
        feat = feat[:seq_len, :]
        if feat.shape[0] < 256:
            feat = np.concatenate([feat, np.zeros((256 - feat.shape[0], feat.shape[1]), dtype=np.float32)], axis=0)

        feat = feat[None, ...]
        
        wav_name = os.path.splitext(os.path.basename(wav_path))[0]
        npy_path = f'{args.output_path}/{wav_name}.npy'
        np.save(npy_path, feat)
        tf.add(npy_path)
    
    tf.close()
    print(f'Save calib dataset to calib.tar.gz')

if __name__ == '__main__':
    main()