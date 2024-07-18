from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
def train_knn(X_train, y_train, k):
    knn = KNeighborsClassifier(n_neighbor=3).fit(X_train, y_train)
    return knn

def train_Kmean(X_train, y_train, k):
    km = KMeans(n_clusters=2).fit(X_train)
    return km
tokenized_sentences = [
    'virus máy_tính',
    'máy_tính nhiễm virus',
    'xuất_hiện virus mới trên điện_thoại_di_động',
    'máy_tính thường sẽ chậm khi bị nhiễm virus'
]

# counter = CountVectorizer(min_df=1)#đếm tuần suất từ xuất hiện
# tf_matrix = counter.fit_transform(tokenized_sentences)#truyền vào 
counter = CountVectorizer().fit_transform(tokenized_sentences)

print(counter.__dict__)
v = TfidfVectorizer()
vector = v.fit_transform(tokenized_sentences)
# print(vector.todense())