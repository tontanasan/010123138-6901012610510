class Person :
    def __init__(self, name, adress, wight, higth):
        self.name= name
        self.adress= adress
        self.wight = wight
        self.higth = higth
        
    def __str__(self):
        return f"name:{self.name}\nadress:{self.adress}\nwight:{self.wight}\nhigth:{self.higth}"
    def show(self):
        print(self)
    
p1=Person("ton","kmutnb",70,178)
p1.show()
