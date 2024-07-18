#một số biến cơ bản
a = "name" #str
a = 3 #int
a = 3.5#float
a = 1j#complex
#Tạo số phức
a = complex(5,1)
print (a)

a = ["apple", "banana", "cherry"] #list
a = ("apple", "banana", "cherry") #tuple
a = {"apple", "banana", "cherry"} #set
a= {"name":"John","Age":36}#dict
a = True #bool
# Sử dụng dấu ngoặc nhọn
my_set = {1, 2, 3, 4, 5}

# Sử dụng hàm set()
another_set = set([1, 2, 3, 4, 5])

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Hợp của hai set
union_set = set1.union(set2)  # hoặc sử dụng toán tử |
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Giao của hai set
intersection_set = set1.intersection(set2)  # hoặc sử dụng toán tử &
print(intersection_set)  # Output: {3}

# Phần tử chênh lệch giữa hai set
difference_set = set1.difference(set2)  # hoặc sử dụng toán tử -
print(difference_set)  # Output: {1, 2}

