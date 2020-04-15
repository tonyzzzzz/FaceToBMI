# import numpy as np
# import pandas as pd
import torch
# import matplotlib.pyplot as plt
# from torch import nn, optim
from torchvision import datasets, transforms, models, utils
import torch.nn.functional as F
# from torch.autograd import Variable
# import time
# from glob import glob
# from torch.utils.data.sampler import SubsetRandomSampler
# from collections import OrderedDict
from torch.utils.data import Dataset, DataLoader
from PIL import Image
# import sys

data_transforms = {
    "default": transforms.Compose([
        transforms.Resize(224),
        transforms.ToTensor()
    ]),
    'train': transforms.Compose([
        transforms.RandomRotation(30),
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406),(0.229, 0.224, 0.225))
        ]),
    'val': transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),
    'test': transforms.Compose([
        transforms.Resize(255),
        transforms.CenterCrop(224),
        transforms.ToTensor()
        ]),
}

class FaceToBMIDataset(Dataset):
    def __init__(self, csv_file, image_dir):
        self.annotaion = pd.read_csv(csv_file)
        self.image_dir = image_dir
        self.set_transform()

    def __len__(self):
        return len(self.annotaion)

    def set_transform(self, type=None):
        if type == "train":
            print('Using train transformation')
            self.transform = data_transforms['train']
        elif type == "val":
            print('Using validation transformation')
            self.transform = data_transforms['val']
        elif type == "test":
            print('Using validation transformation')
            self.transform = data_transforms['test']
        else:
            print('Using default transformation')
            self.transform = data_transforms['default']


    def __getitem__(self, idx):
        if torch.is_tensor(idx): idx = idx.tolist()
        img_path = self.annotaion.iloc[idx,0]
        image = Image.open(img_path)
        image = self.transform(image)    
        height = torch.from_numpy(self.annotaion.iloc[idx, 1].reshape(-1,1).squeeze(axis=1)).float()
        weight = torch.from_numpy(self.annotaion.iloc[idx, 2].reshape(-1,1).squeeze(axis=1)).float()
        bmi = torch.from_numpy(self.annotaion.iloc[idx, 3].reshape(-1,1).squeeze(axis=1)).float()
        return image, height, weight, bmi