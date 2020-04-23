import numpy as np
import pandas as pd
import sys

class Config:
    # Set up Variable
    data_path = "../data/"
    raw_data_path = data_path + "raw/"
    intermediate_data_path = data_path + "interim/"
    full_annotation_name = intermediate_data_path + "full_annotation.csv"
    female_annotation_name = intermediate_data_path + "female_annotation.csv"
    male_annotation_name = intermediate_data_path + "male_annotation.csv"
    batch_size = 16

    image_dir = data_path+"images/"

    processed_path = "../data/processed/"

    base_learning_rate = 1e-5
    epochs = 1 #should be 500 change to 400000 if you are a rich kid!
    weight_decay = 0.0005
    gamma = 0.001
    power = 0.75
    num_of_tries = 5

cfg = Config()