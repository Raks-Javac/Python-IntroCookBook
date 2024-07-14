#  This file is to explain exceptions in python 
class Division:
    def __init__(self,denominator,numerator) :
        self.denominator = denominator
        self.numerator = numerator
    def calculate(self):
        try: 
            return self.numerator/self.denominator
        except ZeroDivisionError:
            print("Error while running division")


# This throws an error because 100 is not divisible by 
print(Division(0,100).calculate())
# This below doesnt 
print(Division(2,20).calculate())
    

