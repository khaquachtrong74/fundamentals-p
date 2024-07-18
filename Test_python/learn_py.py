
#df = pd.read_csv("D:\My_Self_Studying\C++\Large_Task_NMLT_2023\Data_Bienso.txt", sep ='\t', header = None)
#print(df)
#print("Data tổng hợp từ chương trình mô phỏng bãi đậu xe")
#df_2 = pd.read_csv("D:\My_Self_Studying\C++\Large_Task_NMLT_2023\Data_TongHop.txt")
#print(df_2)


#Thư viện pandas_ phân tích dữ liệu, xử lý dự liệu dưới dạng bảng
import pandas as pd

#Đọc dữ liệu từ file CSV
#có thể chỉnh 1 số thứ như header = none, sep = ',', hoặc gán đường dẫn tới file
#df = pd.read_csv('name_.txt')

#Tạo DataFrame từ dictionary
data ={'Tên':['Kha','Quách ca ca','Tiểu Quạch','Quách Quằn Quại'],
       'Tuổi':[12, 24, 45, 56]}
df = pd.DataFrame(data)
print("In ra đầu 5 dòng đầu")
#Hiển thị dữ liệu với 5 dòng đầu tiên
print(df.head())
print("In ra đuôi 5 dòng cuối")
#Hiển thị dữ liệu với 5 dòng cuối
print(df.tail())
print("In ra tất cả")
#Hiện thị toàn bộ
print(df)

#Một số thao tác trên dữ liệu

#lọc dữ liệu 
filtered_data = df[df['Tuổi'] > 17]
print("sau khi lọc dữ liệu tuổi > 17")
print(filtered_data)

#Thêm cột mới
df['Job'] = ['Ma pháp sư','Kiếm sư','Ma thuật sĩ','Thương sĩ']
print("Sau khi thêm cột job")
print(df);

#Xoá cột
df.drop(columns=['Tuổi'], inplace = True)

#Xuất dữ liệu thành các định dạng file
#CSV
#df.to_csv('Declaired.csv', index=False)
#Excel
#df.to_csv('Output.xlsx', index=False)

#Thao tắt cắt dữ liệu
#lấy hàng từ 1 tới 3 và cột 0 đến 2
slice_df = df.iloc[1:3, 0:2]
print('sau khi lấy hàng 1-3 và cột 0-2')
print(slice_df)
#lấy hàng có nhãn với .loc



#nối 2 dataframe lại vào nhau
df1 = pd.DataFrame({'A':[1,2],'B':[5,12]})
df2 = pd.DataFrame({'A':[5,6],'B':[2,1]})

result = pd.concat([df1,df2])
print(result)
#Cách trên sẽ vẫn dữ nguyên chỉ mục cột của 2 dataframe thành 0,1,0,1 thay vì 0,1,2,3
#cách sửa
result = pd.concat([df1,df2], ignore_index = True)
#nếu để thành false thì sẽ như cũ giữ nguyên chỉ số index của 2 dataframe
print(result)


df_k = pd.read_csv('Output.xlsx')
print("Dữ liệu ban đầu")
print(df_k)

#THêm cột
df_k['Tiền'] = [10, 20, 30 ,40]

#Thay đổi giá trị
for i in range(0,4):
    df_k.at[i,'Tuổi'] = int(12*i+12)
print("Sau khi thay đổi vài thứ")
print(df_k)


# GHi dataframe vào một file mới
#df.to_csv("name_.txt", index = False) để Index = False là để không cho chỉ mục của dataframe vào file
