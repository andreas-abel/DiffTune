#!/usr/bin/env python3

import argparse
import cloudpickle as pickle
import numpy as np
import os

def main():
    parser = argparse.ArgumentParser(description='Gather data for training')
    parser.add_argument('csv', help="csv file")
    parser.add_argument('-train', action='store_true')
    parser.add_argument('-val', action='store_true')
    parser.add_argument('-test', action='store_true')
    args = parser.parse_args()

    with open(os.path.join(os.path.dirname(os.path.abspath(os.path.realpath(__file__))), '../data/artifacts/blocks'), 'rb') as f:
        blocks = pickle.load(f).reset_index()

    all_idxs = list(blocks['idx'])
    np.random.RandomState(0).shuffle(all_idxs)
    train_idxs = all_idxs[:int(0.8 * len(all_idxs))]
    val_idxs = all_idxs[int(0.8 * len(all_idxs)):int(0.9 * len(all_idxs))]
    test_idxs = all_idxs[int(0.9 * len(all_idxs)):]

    train_set = set(blocks[blocks['idx'].isin(set(train_idxs))].hex)
    val_set = set(blocks[blocks['idx'].isin(set(val_idxs))].hex)
    test_set = set(blocks[blocks['idx'].isin(set(test_idxs))].hex)

    with open(args.csv, 'r') as f:
        lines = f.read().splitlines()

    print(lines[0])
    for line in lines[1:]:
        hex = line.split(',')[0]
        if args.train and (hex in train_set):
            print(line)
        if args.val and (hex in val_set):
            print(line)
        if args.test and (hex in test_set):
            print(line)

if __name__ == '__main__':
    main()
