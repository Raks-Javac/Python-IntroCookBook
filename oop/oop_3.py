#Abstraction 
# Encapsulation 
# Polymorphism


class Item:
    pass


# Phone inherits properties of Item
class Phone(Item):
    pass




class HardDisk:
    pass


class Keyboard:
    pass


# laptops inherits hard disk properties and keyboard properties 

class Laptop(HardDisk,Keyboard):
    pass




# Setters and getters in python


class Student: 
    def __init__(self,name, matric_number):
        self.__name = name
        self.__matric_number = matric_number

# getter
    @property
    def name(self):
        return self.__name 
    @property
    def matric_number(self):
        return self.__matric_number
    
    # setter
    @name.setter
    def name(self,value):
        self.__name = value

#private method
    def __run_admission(self) -> bool:
        return self.__name != "" and self.__matric_number != "" 
    
    def send_admission(self):
        if(self.__run_admission):
            return f"Congratulations {self.name}, you've been admitted" 
        else:
            return f"Admission processing"
    
        

sttudent = Student("John",9202928292)
print(sttudent.send_admission()) 