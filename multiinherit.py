#multiple inheritance means one child class will have more than one parent class to inherit from
class Employee:
    def __init__(self,name):
        self.name=name
class Dancer:
    def __init__(self,dance):
        self.dance=dance    
class danceremployee(Employee,Dancer):
    def __init__(self,name,dance):
        self.name=name
        self.dance=dance
        print(f"{self.name},{self.dance}")
f=danceremployee("simran","kathak")
print(f.name)
print(f.dance)    
print(danceremployee.mro())             
        