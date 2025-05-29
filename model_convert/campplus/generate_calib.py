import os, sys
import argparse
import glob
import numpy as np


def get_args():
    parser = argparse.ArgumentParser(description='Generate calibration dataset for quantization')
    parser.add_argument('--output_path', default='./calib_dataset')
    parser.add_argument('--input_path', default='./data/raw_data/3dspeaker/test')
    parser.add_argument('--max_num', type=int, default=10, help='Max calib data num')
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    
    os.makedirs(args.output_path, exist_ok=True)

    