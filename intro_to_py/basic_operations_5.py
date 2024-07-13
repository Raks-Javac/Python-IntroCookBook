# This file contains basic operations in python
# We would be using the first two variables for our operations


first_number = 2
second_number = 3

# + , - , *
# "/" for division returns a float
# "//" for divisionf but returns an int
#  "%" modulus
# "**" power
# += continuous assignment


print(first_number / second_number)
print(first_number // second_number)
print(first_number % second_number)
print(first_number**second_number)


# Just like bodmas there is operator precedence when computing basic operations
# multiplication and division have a higher order
# multiplication and division computes before additon and subtraction
# perenthesis defaults this
print(first_number + second_number * first_number)
print((first_number + second_number) * second_number)
