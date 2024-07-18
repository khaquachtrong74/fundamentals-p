import numpy as np
A = np.array([[1,0,0],[-3,1,0],[2,1,3]])
B = np.array([[2,-1,3],[0,1,4],[0,0,1]])
detA = np.linalg.det(A)
detB = np.linalg.det(B)
detAB = np.linalg.det(3*A*B)
print(detA)
#a*d - b*c
print(detB)
#Tìm ma trận nghịch đảo (chỉ khi det != 0 thì ta mới tìm được)
Ainv = np.linalg.inv(A)
print(Ainv)
print(detAB)

A = np.array([[1,1,1,1,1],[0,0,0,0,0],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4]])
B = np.array([[1,1,0,1,1],[2,2,0,2,2],[3,3,0,3,3],[4,4,0,4,4],[5,5,0,5,5]])
print(A*B)