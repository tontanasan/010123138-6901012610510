class Person:
    def __init__(self,name,address,wight,height):
        self.name = name
        self.address = address
        self.wight = float(wight)
        self.height = float(height)
        
    def getBMI(self):
        height_m = self.height / 100
        bmi= self.wight / (height_m**2)
        return bmi
        
        
class Employee (Person):
    def __init__(self,name,address,wight,height,employee_id, departmet, salary):
        super().__init__(name,address,wight,height)
        self.employee_id = employee_id
        self.departmet = course
        self.salary = salary
        
    def __str__(self):
        return f"""
name : {self.name}
address : {self.address}
wight : {self.wight}
height : {self.height}
student_id : {self.employee_id}
course : {self.salary}
bmi : {self.getBMI()}
"""
    def show(self):
        print(self.getBMI())
        print(self)

e1=Employee("ton","kmutnb",70,178,111,"computer",15000)
e1.show()
