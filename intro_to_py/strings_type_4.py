#  This file is to understand string as a whole

course_code = "csc 350"

#  functions available in the string object/ data type
# just returns a new string
print(course_code.upper())
print(course_code.find("c"))
print(course_code.capitalize())
print(course_code.replace("c", "q"))


# instead of find , you can use the keyword 'in' to find  too, which returns a bool
# not a new value of strings

print("csc" in course_code)
