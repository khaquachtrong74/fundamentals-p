#dùng wordcloud để trực quan hoá dữ liệu trên barchart - smth
from wordcloud import WordCloud
import matplotlib .pyplot as plt
import pandas as pd
import seaborn as sns
text = "tôi thích ngôn_ngữ lập_trình C++, nó giúp tôi hiểu_rõ bản_chất lập_trình"
wl = WordCloud(width=800, height=400, background_color='white').generate(text)

#plt.figure(figsize=(10, 5))
#plt.imshow(wl, interpolation='bilinear')#Phân bố
#plt.axis('off')#trục
#plt.show()

from collections import Counter #đếm tần suất từ
words = text.replace(",","").split()#Split dùng để cắt

word_freq = Counter(words)#Trả về kiểu dictionarry
#items  trả về (key, value)
print(word_freq)
#df = pd.DataFrame(word_freq.items(), columns=['Word','Frequency'])
#df = df.sort_values(by='Frequency', ascending=False)#ascending= False là giảm dần
#plt.figure(figsize=(15, 7))
#sns.barplot(x='Word',y='Frequency',data=df)
#plt.title('Frequency words')
#plt.show()

#Embedding là một vector (đa chiều >=  2 chiều)
#dùng thuật toán t-SNE chuyển văn bản đa chiều thành 2-3 chiều

