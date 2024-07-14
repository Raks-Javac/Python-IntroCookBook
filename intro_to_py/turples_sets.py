# This file is for turples and sets 



# Tuples are ordered, immutable collections of items. 
# Once a tuple is created, its elements cannot be changed, added, or removed. 
# Tuples are defined by enclosing elements in parentheses ().
# Key Characteristics of Tuples:

#     Ordered: Elements have a defined order.
#     Immutable: Cannot be changed after creation.
#     Allows Duplicates: Can contain duplicate elements.



my_tuple = (2, 1, 4)

print(my_tuple)


#  they can also take multiple data types 


my_tuple = (2, "1", 4)

print(my_tuple)


#  you can also have nested turples 


nested_tuple = (1, (2, 3), (4, 5, 6))

print(f"nested turples {nested_tuple}")

# looping through nested turples 

for i in nested_tuple:
    print(f"{i}",end=" ")



    # ########

# Sets in Python

# Sets are unordered collections of unique items. Sets are mutable, meaning you can add or remove items after creation. Sets are defined by enclosing elements in curly braces {}.
# Key Characteristics of Sets:

#     Unordered: No defined order.
#     Mutable: Can be changed after creation.
#     No Duplicates: Cannot contain duplicate elements.


print()
my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(2)
print(my_set)