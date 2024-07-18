# LinkedIn Learning Python course by Joe Marini
#


# TODO: import the math module, which contains features for working with mathematics
import math

# TODO: the math module contains lots of pre-built functions


# TODO: in addition to functions, some modules contain useful constants 


# TODO: try some of the math functions for yourself here:

import cv2
import numpy as np
import os
from sklearn.neighbors import KNeighborsClassifier

def read_data(path="Data_set\Cat", size=(32, 32)):
    images, labels = [], []

    lbl = 0
    # Biến tạm
    tmp = {}
    for folder_name in os.listdir(path):
        lbl = lbl + 1
        p = f'{path}/{folder_name}'
        for file in os.listdir(p):
            img = cv2.imread(f'{p}/{file}', cv2.IMREAD_GRAYSCALE)
            if img is not None:
                img = cv2.resize(img, size)
                images.append(img)
                labels.append(lbl)
    return np.array(images), np.array(labels)

def train_knn(X, y):
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X, y)
    return knn

if __name__ == '__main__':
    x, y = read_data()
    print(y)
    print(x)
