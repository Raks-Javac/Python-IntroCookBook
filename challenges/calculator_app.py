# This file is for challenges listed below


# ##### Challenge 1

# Calculator Program:
# Create a program that takes in math expressions (e.g., 2+2, 5*3, 7-1) and evaluates them.



# Challege 1 solution 
class CalculatorClass:
    def __init__(self):
        self.sign = ""
        self.first_input = None
        self.second_input = None

    # Checking if the sign is in the system
    def check_sign_on_input(self) -> str:
        signs = ['-', '+', '*', '/']
        sg = str(input("Enter operation sign: "))
        if sg not in signs:
            print("Operation not supported in system")
            return ""
        else:
            self.sign = sg
            return sg

    # Taking the user's first input and catching errors
    def take_first_input(self):
        try:
            self.first_input = float(input("Enter first number: "))
        except ValueError:
            print("Input is not a number")

    # Taking the user's second input and catching errors
    def take_second_input(self):
        try:
            self.second_input = float(input("Enter second number: "))
        except ValueError:
            print("Input is not a number")

    # Running the calculator after checking the sign
    def run_calculator_app(self):
        if self.check_sign_on_input() != "":
            self.take_first_input()
            if self.first_input is not None:
                self.take_second_input()
                if self.second_input is not None:
                    self.calculate()

    # Perform the calculation based on the sign
    def calculate(self):
        if self.sign == '+':
            result = self.first_input + self.second_input
        elif self.sign == '-':
            result = self.first_input - self.second_input
        elif self.sign == '*':
            result = self.first_input * self.second_input
        elif self.sign == '/':
            if self.second_input != 0:
                result = self.first_input / self.second_input
            else:
                print("Cannot divide by zero")
                return
        print(f"The result is: {result}")


#  initialize object
calculator = CalculatorClass();