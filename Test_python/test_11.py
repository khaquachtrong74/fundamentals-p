#Trực quan hoá dữ liệu / matplotlib / seabom / plotly
import matplotlib .pyplot  as plt #thư viện vẽ biểu đồ
import pandas as pd #thư viện xử lý dữ liệu
import numpy as np
import seaborn as sns
data = pd.DataFrame({
    'categories' : ['A','B','C','D'],
    'values' : [10,20,5,30]
})

#plt.figure(figsize=(5,4))#Chỉ định kích thước
# truyền dữ liệu vào từ dataF
#plt.plot(data['categories'],data['values'])# Biểu đồ đường

#plt.bar(data['categories'],data['values'])#Biểu đồ cột
#plt.pie(data['values'], labels=data['categories'], autopct='%1.1f%%')#Biểu đồ tròn
#plt.title('Line Charge')
#plt.xlabel('Categories')
#plt.ylabel('Numb')
#plt.savefig
#plt.show()

#plt.figure(figsize=(5,4))
#sns.scatterplot(x='categories', y='values', data=data)
#plt.title('Tan xa')
#plt.show()

#data_box = pd.DataFrame({
#    'categories':['A']*50 + ['B']*50 + ['C']*50 + ['D']*50, #Nối 2 danh sách,
#    'values' : np.random.randn(200)#random 200 phan tu
#})

#plt.figure(figsize=(12, 7))
#sns.boxplot(x='categories', y='values', data=data_box)
#plt.title('Box chart')
#plt.show()

data_heatmap = np.random.randn(10, 12)
print(data_heatmap)

plt.figure(figsize=(10, 6))
sns.heatmap(data_heatmap, annot=True, cmap='viridis',)
plt.title('heatmap chart')
plt.show()