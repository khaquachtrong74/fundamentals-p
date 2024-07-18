import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import openpyxl
import pprint
path1 = '10.18.2023-11.21.2023(1).xlsx'
data1 = pd.read_excel(path1)

path2 = '10.18.2023-11.21.2023(2).xlsx'
data2 = pd.read_excel(path2)

path3 = '09.20.2023-10.17.2023.xlsx'
data3 = pd.read_excel(path3)

path4 = '08.20.2023-09.19.2023.xlsx'
data4 = pd.read_excel(path4)

data4.columns = data3.columns = data2.columns = data1.columns

df_final = pd.concat([data1,data2,data3,data4],ignore_index=True)

df_final = df_final.drop(0)
df_final.rename(columns={'Unnamed: 3':'Giá trị GD ròng'},inplace=True)
df_final.rename(columns={'Unnamed: 5':'Giá trị mua'},inplace=True)
df_final.rename(columns={'Unnamed: 7':'Giá trị bán'},inplace=True)
df_final.rename(columns={'Giao dịch ròng':'Khối lượng GD ròng'},inplace=True)
df_final.rename(columns={'Mua':'Khối lượng mua'},inplace=True)
df_final.rename(columns={'Bán':'Khối lượng bán'},inplace=True)

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
print(df_final)
#Mua/Bán ở đây là khối lượng mua và khối lượng bán
df_final['Giá trị cổ phiếu'] = df_final.apply(lambda row: row['Giá trị mua']*1000000000 /row['Khối lượng mua'] if row['Khối lượng mua']!= 0 else None, axis = 1)
# dữ liệu của cột giá trị bán
mean_Sell = df_final['Giá trị bán'].mean()
var_Sell  = df_final['Giá trị bán'].var()
std_Sell  = df_final['Giá trị bán'].std()
Q1_Sell   = df_final['Giá trị bán'].quantile(0.25)
Q2_Sell   = df_final['Giá trị bán'].quantile(0.5)
Q3_Sell   = df_final['Giá trị bán'].quantile(0.75)
min_Sell  = df_final['Khối lượng bán'].min()
max_Sell  = df_final['Khối lượng bán'].max()

# dữ liệu của cột giá trị mua
mean_Buy = df_final['Giá trị mua'].mean()
var_Buy  = df_final['Giá trị mua'].var()
std_Buy  = df_final['Giá trị mua'].std()
Q1_Buy   = df_final['Giá trị mua'].quantile(0.25)
Q2_Buy   = df_final['Giá trị mua'].quantile(0.5)
Q3_Buy   = df_final['Giá trị mua'].quantile(0.75)
min_Buy  = df_final['Khối lượng mua'].min()
max_Buy  = df_final['Khối lượng mua'].max()

#netT: net transactions = GD ròng
mean_netT = df_final['Khối lượng GD ròng'].mean()
var_netT  = df_final['Khối lượng GD ròng'].var()
std_netT  = df_final['Khối lượng GD ròng'].std()
Q1_netT   = df_final['Khối lượng GD ròng'].quantile(0.25)
Q2_netT  = df_final['Khối lượng GD ròng'].quantile(0.5)
Q3_netT   = df_final['Khối lượng GD ròng'].quantile(0.75)
min_netT  = df_final['Khối lượng GD ròng'].min()
max_netT  = df_final['Khối lượng GD ròng'].max()

# câu 4 với dataframe "caculator" chứa các giá trị: Trung bình, phương sai,độ lệch chuẩn và tứ phân vị
caculator = {'Trung bình':[mean_Buy,mean_Sell,mean_netT],
             'Phương sai':[var_Buy,var_Sell,var_netT],
             'Độ lệch chuẩn':[std_Buy,std_Sell,std_netT],
              'Q1':[Q1_Sell,Q1_Buy,Q1_netT],
              'Q2':[Q2_Sell,Q2_Buy,Q2_netT],
              'Q3':[Q3_Sell,Q3_Buy,Q3_netT],
              'Min':[min_Buy,min_Sell,min_netT],
              'Max':[max_Buy,max_Sell,max_netT]}
caculator = pd.DataFrame(caculator, index=['Khối lượng mua:','Khối lượng bán:','Khối lượng giao dịch ròng:'])

chuthich = {'':['Chú thích: Q1, Q2, Q3 là giá trị của tứ phân vị','Đơn vị của giá trị cổ phiếu là Vnđ']}
ct = pd.DataFrame(chuthich, index =['',''])

print(df_final)
print(caculator)
print(ct)

x = df_final['Ngày']
y = df_final['Khối lượng mua']/len(df_final['Khối lượng mua'])
z = df_final['Khối lượng bán']/len(df_final['Khối lượng mua'])
arr = np.array([0]*len(df_final['Ngày']))
plt.plot(x, z, label='lượng cổ phiếu bán ra khối ngoại',color='blue')
plt.plot(x, y, label='lượng cổ phiếu mua vào khối ngoại',color = 'red')
plt.plot(x,arr,label ='Số lượng mua, bán chạm đáy')
plt.xticks(rotation=30)
plt.title('Xu hướng mua, bán của khối ngoại mã VNM')
plt.legend()
plt.show()




