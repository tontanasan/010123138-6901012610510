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
        
        
class Student (Person):
    def __init__(self,name,address,wight,height,student_id,course,gpa):
        super().__init__(name,address,wight,height)
        self.student_id = student_id
        self.course = course
        self.gpa = gpa
        
    def __str__(self):
        return f"""
name : {self.name}
address : {self.address}
wight : {self.wight}
height : {self.height}
student_id : {self.student_id}
course : {self.course}
bmi : {self.getBMI()}
"""
    def show(self):
        print(self.getBMI())
        print(self)

p1=Student("ton","kmutnb",70,178,111,"cpre",2.5)
p1.show()