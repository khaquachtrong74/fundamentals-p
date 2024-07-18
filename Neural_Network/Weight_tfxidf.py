# from sklearn.cluster import KMeans
# from sklearn.neighbors import KNeighborsClassifier

# tokenized_sentences = [
#     ['Virus', 'máy tính'],
#     ['máy tính', 'nhiễm', 'virus'],
#     ['xuất hiện', 'virus', 'mới', 'trên', 'điện thoại di động'],
#     ['tài liệu', 'về', 'máy tính'],
#     ['máy tính', 'thường', 'sẽ','chậm','khi','bị','nhiễm','virus']
    
# ]
# #phân loại
# def train_knn (X_train, y_train):
#     knn = KNeighborsClassifier(n_neighbors=3).fit(X_train, y_train)
#     return knn
# #gom cụm
# def train_kmeans(X_train):
#     kmeans = KMeans(n_clusters=2, random_state=0).fit(X_train)
#     return kmeans

# from gensim import corpora
# vocabs = corpora.Dictionary

