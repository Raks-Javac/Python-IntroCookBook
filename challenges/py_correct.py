# # Task1 create a calculator that takes in math expresssion and returns the result

# # function to take input

# x = 0
# y = 0

# def take_input():
#     a = int(input('Enter first number: '))
#     b = int(input('Enter second number: '))
#     return [a,b]



# print('ADDITION')
# # addition
# def add(x, y):
#     return x + y



# # subtraction
# print('SUBTRACTION')
# def subtract(a, b):
#     return a-b

# # multiplication
# print('MULTIPLICATION')
# def multiply(p, q):
#     return p*q

# # division
# print('DIVISION')
# def divide(r, s):

#     if s == 0:
#         return "Error! Division by zero is not allowed."
#     else:
#         return r/s

# print('POWER')
# def power(m, n):
#     return m**n

# print('SQUARE-ROOT')
# def square_root(z):
#     if z < 0:
#         return "Error! Square root of negative number is not allowed."
#     else:
#         return z**0.5




# Task1 create a calculator that takes in math expresssion and returns the result


print('ADDITION')
# addition
def add(x, y):
    return x + y
x= int(input('Enter a value for x: '))
y= int(input('Enter a value for y:'))
print(f'result: {add(x,y)}')

# subtraction
print('SUBTRACTION')
def subtract(a, b):
    return a-b
a= int(input('Enter a value for a: '))
b= int(input('Enter a value for b: '))
print(f'Result: {subtract(a,b)}')

# multiplication
print('MULTIPLICATION')
def multiply(p, q):
    return p*q
p= int(input('Enter a value for p: '))
q= int(input('Enter a value for q: '))
print(f'Result: {multiply(p,q)}')

# division
print('DIVISION')
def divide(r, s):

    if s == 0:
        return "Error! Division by zero is not allowed."
    else:
        return r/s
r= int(input('Enter a value for r: '))
s= int(input('Enter a value for s: '))
print(f'Result: {divide(r,s)}')

print('POWER')
def power(m, n):
    return m**n
m= int(input('Enter a value for m: '))
n= int(input('Raised to the power of: '))
print(f'Result: {power(m,n)}')

print('SQUARE-ROOT')
def square_root(z):
    if z < 0:
        return "Error! Square root of negative number is not allowed."
    else:
        return z**0.5
z= int(input('Enter a value for z: '))
print(f'Result: {square_root(z)}')