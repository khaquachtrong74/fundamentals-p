import numpy as np
#Matrix
A = np.array([[1, 5, 6], [3, 4, 1], [1, 2, 3]])
print(A)
print(2**A)
print(A**2)

a = np.array([[1, 5], [3, 4]])
b = np.array([[-1, 5], [5, -2]])

#Cong 2 ma tran
print(a+b)

# Nhan 2 ma tran (element-wise)
print(a*b)

#Chuyển vị ma trận (đổi cột thành dòng - dòng thành cột)
A = np.array([[1, 5, 6], [3, 4, 1], [1, 2, 3]])
B = A.T
# dùng hàm
C = np.transpose(A)
print(A)
print(B)
#B == C
print(C)


A = np.array([[1, 5, 6], [3, 4, 1]]) 
#đổi 
B = np.reshape(A, (3, 2) )
# để số đuôi / đầu thành -1 thì np sẽ tự tính số dòng/ cột
print(A)
print(B)
B = np.reshape(A, (3, -1) )
print(B)

A = np.array([[1, 5, 6, -2], [3, 4, 1, 2]])
X = np.array([2, 3, -1, -2])
print(A+X)
print(A*X)

A = np.array([[1, -2, 1], [2, 3, 4]])
B = np.array([[1, 2], [2, 4], [5, -2]])
#Điều kiện nhân 2 ma trận
C = np.dot(A, B)
print(C)