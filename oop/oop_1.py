#  this file is mainly to show differences around __str__ , __repr__ and __dict__

class Student: 
    teacher_name = "Josh"
    def __init__(self,student_name: str = "Default name",student_number: int =1):
        assert student_name != "", f"Student name is empty"

        # Assign to self object
        self.student_name : str | None = student_name
        self.student_number: int | None = student_number

    def __str__(self) -> str:
        return f"Four"
    
    # shows representation of the current object 
    def __repr__(self):
        return f"Student(name={Student.teacher_name})"
        

        
    
student1 = Student("Joan",student_number=19283)

# __dict__ gets all the attributes of an object
print(f"Class level attribute {Student.__dict__}")
print(f"Instance level attribute {student1.__dict__}")
print(student1.__repr__)