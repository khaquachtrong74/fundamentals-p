#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

# class connguoi():
#     def __init__(self, Ten):
#         self.Ten = Ten # xác định giá trị thuộc tính của lớp PhuongTien
# #Kế thừa
# class Sinhvien(connguoi):
#     def __init__(self, Ten, mssv):
#         super().__init__("Tre")
#         self.mssv = mssv
#         self.Ten = Ten

# class GiangVien(connguoi):
#     def __init__(self, Ten, Luong):
#         super().__init__("Giao su")

# sv = Sinhvien("Kha", 2351050070)

# print(sv.mssv)
# print(sv.Ten)
        
        
        
class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

class Car(Vehicle):
    def __init__(self, eginetype):
        super().__init__("Car123")# truyền thông tin/ đối số này vào bodystyle trong lớp Vehicle
        self.wheels = 4
        self.doors = 4

        self.eginetype = eginetype
        
class Motorcycle(Vehicle):
    def __init__(self, eginetype, hassidecar):
        super().__init__("Motorcycle")
        if(hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.eginetype = eginetype
    #Phương thức
    def move(self, speed):
        self.speed = speed
        return f"This {self.eginetype} can move {self.speed} km/h"
        
test = Vehicle("Plane")
car = Car("G63")
print(car.bodystyle)
print(car.wheels)
print(test.bodystyle)

moto = Motorcycle("Sun", False)
print(moto.move(24))