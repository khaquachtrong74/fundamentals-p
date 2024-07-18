from pyvi import ViTokenizer, ViPosTagger
# asf
Q = "Virus máy tính"


D1 = "Máy tính bị nhiễm Virus"
D2 = "Xuất hiện virus mới trên điện thoại di động"
D3 = "Tài liệu về máy tính"
D4 = "Máy tính thường sẽ chậm khi bị nhiệm virus"

data = [
    "Virus máy tính",
    "Máy tính bị nhiễm Virus",
    "Xuất hiện virus mới trên điện thoại di động",
    "Tài liệu về máy tính",
    "Máy tính thường sẽ chậm khi bị nhiễm virus",
    ]
#import Counter để đếm tần suất xuất hiện của từ
from collections import Counter
import numpy as np
import math
#tokens_D1 = ViTokenizer.tokenize(D1)
#pos_D1 = ViPosTagger.postagging(tokens_D1)
array = []
#print(pos_D1)


# heuristic (Tần số xuất hiện càng lớn thì độ quan trọng càng cao)// dùng cosine
def preprocess(data):
    for sentences in data:
        token_D = ViTokenizer.tokenize(sentences.lower())
        pos_D = ViPosTagger.postagging(token_D)
        array.append(token_D.split())
    return array
def get_vocabularies(tokenized_docs):
    vocabs = set()
    '''Hàm set thì nó như 1 cái list nhưng các đối tượng trong đó
        sẽ không có trùng nhau (tức là xuất hiện 1 lần), ta sẽ dùng đặc tính này
        để xác định tần xuất số từ trong tokenized_docs(array)
        '''
    for docs in tokenized_docs:
        vocabs.update(docs)
    return vocabs

#hàm tạo vector
def create_vectors(one_docs, vocabs):
    word_count = Counter(one_docs)
    return np.array([word_count[w] for w in vocabs])

def cosine_similarity(x_vec, y_vec):
    dot_product = np.dot(x_vec, y_vec)
    norm_vec1 = np.linalg.norm(x_vec)
    norm_vec2 = np.linalg.norm(y_vec)

    return dot_product / (norm_vec1*norm_vec2)

#tính idf của mỗi từ
def caculate_idf(tokenized_docs, vocabs):
    #idf = log(n/df)
    n = len(data)
    idf = {} #từ điển : dict
    for word in vocabs:
        #df là số tài liệu trong kho tài liệu có chứa từ này
        df = sum([ 1 for doc in tokenized_docs if word in doc])
        idf[word] = math.log(n/df)
        #hãy xem idf như 1 map vậy và các word sẽ là các key, nhập key trả về giá trị
    return idf

#Tạo ra vector idf để nhân với vector gốc (tf)
def create_vectors_idf(one_docs, idf, vocabs):
    vector = np.zeros(len(vocabs))
    for idx, word in enumerate(vocabs):
        if word in one_docs:
            vector[idx] = idf[word]
    return vector #vector idf
if __name__ == '__main__':
    tokenized_docs = preprocess(data)
    vocabs = get_vocabularies(tokenized_docs)
    #print(tokenized_docs)
    #print(vocabs)#len(vocabs) = 14
    idf = caculate_idf(tokenized_docs, vocabs)
    vectors = [create_vectors(doc, vocabs)*create_vectors_idf(doc, idf, vocabs)  for doc in tokenized_docs]
    # lý do nhân với vector idf là nhằm tăng hình phạt lên các từ xuất hiện nhiều trong tất cả tài liệu

    print(vectors)
    #print(tokenized_docs)
    #print(vectors[0])
    #print(vectors[1])
    #print(vectors[2])
    #print(vectors[3])
    #print(vectors[4])
    #term frequency -> tf = thể hiện tầm quan trọng của một từ 
    #cải tiến phần tần số
    #df -> document frequency df(may tinh) = 2
    # idf -> inverse document frequency idf = log(n/df)
    #sự xuất hiện của từ càng nhiều thì độ ưu tiên cao
    #dựa vào kinh nghiệm thì nếu mà 1 từ xuất hiện nhiều trong một
    #tài liệu thôi thì thường đó là cái từ quan trọng, nhưng nếu nó xuất
    #hiện nhiều trong tất cả các tài liệu khác thì thường từ đó không có ý nghĩa
    '''
    tf * idf(penalty) : thể hiện sự tăng tiến cái tỉ lệ thuận và idf ở đây sẽ là hình phạt cho
    khả năng tần số xuất hiện của tf ( nếu từ đó xuất hiện trong 1 tài liệu thì trọng số sẽ
    rất lớn, đồng thời từ đó cũng xuất hiện trên nhiều tài liệu khác thì df càng lớn => idf càng nhỏ
    
    '''
    """
    Q = "Virus máy tính"
    D1 = "Máy tính bị nhiễm Virus"
    D2 = "Xuất hiện virus mới trên điện thoại di động"
    D3 = "Tài liệu về máy tính"
    D4 = "Máy tính thường sẽ chậm khi bị nhiệm virus"
    """
    print('\n')
    print(cosine_similarity(vectors[0], vectors[1]))
    print(cosine_similarity(vectors[0], vectors[2]))
    print(cosine_similarity(vectors[0], vectors[3]))
    print(cosine_similarity(vectors[0], vectors[4]))


    #Phân lớp / classification / supervised
    #Gom cụm / clustering / unsupervised
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters = 4, random_state = 0).fit(vectors)
    #import pdb
    #pdb.set_trace() nó sẽ dừng ở đây và cho ta coi kết quả (như debug)
    print(kmeans.__dict__)# in hết tất cả các thuộc tính
    
