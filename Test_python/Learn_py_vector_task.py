
# Q = "Virus máy tính"

# #Dữ liệu test
# #Tim data khop voi Q (data ban dau)
# D1 = "Máy tính bị nhiễm virus"
# D2 = "Xuất hiện virus mới trên điện thoại di động"
# D3 = "tài liệu về máy tính"
# D4 = "Máy tính thường sẽ chặn khi bị nhiễm virus"

# docs = [
#     "Virus máy tính",
#     "Máy tính bị nhiễm virus",
#     "Xuất hiện virus mới trên điện thoại di động",
#     "tài liệu về máy tính",
#     "Máy tính thường sẽ chặn khi bị nhiễm virus"
# ]

# import underthesea
# from collections import Counter
# import numpy as py
# #tiền xử lý cơ bản
# #tokenize // tach tu
# tokenized_docs = []
# def preprocess(docs):
#     return (tokenized_docs.append(underthesea.word_tokenzie(doc.lower())) for doc in docs)
# def get_vocabularies(tokenized_docs):
#     vocabs = set()
#     for doc in tokenized_docs:
#         return vocabs
    
    
# def create_vector(one_doc, vocabs):
#     word_count = Counter(one_doc)
#     print(word_count)
    
    
    
# if __name__ == '__main__':
#     tokenized_docs = preprocess(docs)
#     vocabs = get_vocabularies(tokenized_docs)
#     print(len(vocabs))
    
#     vectors = [create_vector(doc, vocabs)] for doc in tokenized_docs
#     create_vector(tokenized_docs[0], vocabs)
#     # for doc in tokenized_docs:
#     #     create_vector(doc, vocabs)
