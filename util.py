import numpy as np
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from matplotlib import pyplot as plt

class RandomCrop():
    def __init__(self, output_size): #(256, 512)
        self.output_size = output_size

    def __call__(self, sample):
        new_h, new_w = self.output_size
        h, w, _ = sample['left'].shape
        top = np.random.randint(0, h - new_h)
        left = np.random.randint(0, w - new_w)

        for key in sample:
            sample[key] = sample[key][top: top + new_h, left: left + new_w]

        return sample

class ToTensor():

    def __call__(self, sample):
        left = sample['left']
        right = sample['right']

        sample['left'] = torch.from_numpy(left.transpose([2, 0, 1])).type(torch.FloatTensor)
        sample['right'] = torch.from_numpy(right.transpose([2, 0, 1])).type(torch.FloatTensor)

        if 'disp' in sample:
            sample['disp'] = torch.from_numpy(sample['disp']).type(torch.FloatTensor)

        return sample


class Normalize(): # along first channel
    def __init__(self, mean, std):
        self.mean = torch.tensor(mean).view(-1,1,1)
        self.std  = torch.tensor(std).view(-1,1,1)

    def __call__(self, sample):
        sample['left'] = (sample['left'] - self.mean) / self.std
        sample['right'] = (sample['right'] - self.mean) / self.std
        return sample

def test():
    pass

if __name__ == '__main__':
    test()
    
