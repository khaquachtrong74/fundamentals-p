# name = input('Xin chào tên bạn là gì?')
# movie = input('Bạn thích xem phim gì?')
# print('{} thích xem phim {} :D'.format(name,movie))

a = False
print(a == 0)#true
b = True
print(b == 1)#True
a += b
print(a)#1
print(bool(a))#True
print(bool(a-a))#False
print(bool(a-b))#False
a, b = True, False
print(bool(a*b))#false
print(bool(a*2))#true