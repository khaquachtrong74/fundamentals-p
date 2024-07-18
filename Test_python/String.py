a = 'Hello, World!'
print(a[1])

for x in 'Banana':
    print(x)
#in ra size
print(len(a))

#Check String   
txt = 'The best things in life are free!'
print('free' in txt)# trả về true khi tìm thấy (như hàm find())

#if/else statement:
if 'free' in txt:
    print("Yes, 'free' is present.")

#not in / không có thì trả về true
print('ne' not in txt)
if 'ne' not in txt:
    print("No, 'ne' is NOT present.")
#Slicing Strings/ ngắc đoạn [a:b]
print(a[2:5])
#Ngắt đoạn từ đầu tới b [:b]
print(a[:7])
#ngắt đoạn từ a tới cuối [a:]
print(a[3:])
#negative Indexing/ dùng chỉ số âm để chỉ vị trí
print(a[-5:-2])
#In hoa
print(a.upper())
#in Thuong
print(a.lower())
#Remove Whitespace/ loại bỏ khoảng trắng
a = ' Hello, World! '
print(a.strip())
#Thay Thế 
print(a.replace('e','k'))
#Split String/ Tách Chuỗi
print(txt.split())

a = 'NENENE'
#In Hoa ký tự đầu và còn lại là thường
print(a.capitalize())
#Chuyển đổi chuỗi thành chữ thường
print(a.casefold())
#Trả về chính giữa chuỗi
print(a.center(2," "))