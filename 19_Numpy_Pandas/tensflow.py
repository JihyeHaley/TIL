import tensflow as tf
import numpy as np
import os
from sklearn.model_selection import train_test_split

import json


DATA_IN_PATH = './data_in/'
DATA_OUT_PATH = './data_out/'


TRAIN_Q1_DATA_FILE = 'train_q1.npy'
TRAIN_Q2_DATA_FILE = 'train_q2.npy'
TRAIN_LABEL_DATA_FILE = 'train_label.npy'
DATA_CONFIGS = 'data_configs.json'
