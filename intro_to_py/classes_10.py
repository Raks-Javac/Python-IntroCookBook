class Class: 
    def __init__(self,name,age) -> None:
        self.name= name
        self.age = age
    
    def get_studentt_info(self):
        print(f"{self.name}")
        print(f"{self.age}")



# initialize the class with properties
student_in_class = Class("Lange",39)


#  run a method in the class 
student_in_class.get_studentt_info()
    