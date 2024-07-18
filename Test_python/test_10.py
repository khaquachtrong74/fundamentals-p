from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans

# Define your sentences
sentences = [
    "Tôi thích ngôn_ngữ lập_trình python",
    "máy_học đang thay_đổi thế_giới",
    "Chúng_ta đang sống trong kỷ_nguyên của trí_tuệ nhân_tạo",
    "python là ngôn_ngữ lập_trình mạnh_mẽ"
]

# Load the model
model = SentenceTransformer('keepitreal/vietnamese-sbert')

# Encode the sentences
embeddings = model.encode(sentences)

# Print the embeddings
print(embeddings)

# Define the number of clusters
num_clusters = 2

# Apply KMeans clustering
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(embeddings)

# Get the cluster assignments
cluster_assignments = kmeans.labels_

# Print the cluster assignments
print(cluster_assignments)
