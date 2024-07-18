c = {2, 3, 4, 5}
print(c)

d = {
    "name" : "kha",
    "year" : 2012,
}
#lặp trên từ điển
for key, value in d.items():
    print(f"{key}:{value}")


a = [1, 2, 3, 4]
b = ["A", 'B', 'C', 'D']

for x, y in zip(a, b):
    print(f"{x}:{y}")