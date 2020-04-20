import numpy as np
import pandas as pd
import sys

class Config:
    # Set up Variable
    data_path = "../data/"
    raw_data_path = data_path + "raw/"
    intermediate_data_path = data_path + "interim/"
    full_annotation_name = intermediate_data_path + "full_annotation.csv"
    batch_size = 16

cfg = Config()