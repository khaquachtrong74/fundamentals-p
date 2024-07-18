import matplotlib .pyplot as plt
from sklearn.manifold import TSNE
import numpy as np

embeddings = np.random.randn(40, 100)
labels = [f'Word{i}'for i in range(40)]
print(labels)
#n_components số chiều
tsne = TSNE(n_components=2, random_state=42)
reduce_embeddings=tsne.fit_transform(embeddings)#Rút gọn không gian còn 2 chiều

plt.figure(figsize=(10, 6))
plt.scatter(reduce_embeddings[:, 0], reduce_embeddings[:,1])#Lấy hết tất cả phần tử trong cột 0 và cột 1

#Dùng enumerate để vừa lấy trị số vừa lấy giá trị
for i, label in enumerate(labels):
    plt.annotate(label,(reduce_embeddings[i,0],reduce_embeddings[i,1]))
#perplexity    
#plt.title("Embedding Visualization")
#plt.show()
