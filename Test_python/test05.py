#demo nhận dạng khuôn mặt
#pip install opencv-python
import cv2
import numpy as np
import os
import sklearn 
from sklearn.manifold import Knn
img = cv2.imread('D:\My_Self_Studying\Python\Data_set\img_01.jpg', cv2.IMREAD_GRAYSCALE)
#Ma trận trắng đen
# print(img.shape)
# print(img)
#Coi ảnh
# cv2.imshow("Grayscale ", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

def read_data(path="Data_set\Cat", size=(32,32)):
    images, labels = [], []
    
    lbl = 0
    #Biến tạm
    tmp = {}
    for folder_name in os.listdir(path):
        lbl = lbl + 1
        p = f'{path}{folder_name}'
        for file in os.listdir(p):
            img = cv2.imread(f'{p}/{file}', cv2.IMREAD_GRAYSCALE)
            if img is not None:
                img = cv2.resize(img, size)
                images.append(img)
                labels.append(lbl)
    return np.array((images)), np.array(labels)

def train_knn(X, y):
    knn = KNeighnorsClassifier(n_neighbors=3)
    knn.fit(X, y)
    return knn

if __name__ == '__main__':
    x, y = read_data()
    print(y)
    print(x)