# This file is for list and list methods 
cars_number = [2,3,4,5,6,3,2,4,4,]



cars_number.append(2)

print(cars_number)
# returns the number of occurrences of "4" in the list 
print(cars_number.count(4))

# other list methods 
len(cars_number)


# for loop operation on a list and list tips and techniques 


# returns all the element before the element with index 2 in the list
print(cars_number[:2])


# returns all the element after the element with index 2 in the list
print(cars_number[2:])

# returns all the element beteen the element with index 2 and the length of the element
print(cars_number[2:len(cars_number)])


# for loops on list 


for i in cars_number:
    # you can also make conditions on this block
    print(cars_number)


# you can use enumerate to get the index of the element and also the element itself 

for index,element in  enumerate(cars_number):
    # you can also make conditions on this block
    print(f"Index and element respectively {index} and {element}")
      

#  Zip to iterate over two list 
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")


# Workinf with matrixes and iterating over multi-dimensional list 

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in matrix:
    for j in i:
        print(j, end=' ')
    print()


# using range stop or jumps
for i in range(0, 100):  # range(0, 10, 2) generates 0, 2, 4, 6, 8
    if(i%2 == 0 and i != 0): print(i,end=" ")


