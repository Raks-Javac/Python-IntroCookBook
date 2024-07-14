#  this file is for functions



def run_for_print():
    print("running this initial function")
      
run_for_print()



# returning mutiple values
def run_name_age(name, age):
    return name,age



# name, age 
print(run_name_age("Lanke",4))


name,age = run_name_age("Lanke",20)
name2,age2 = run_name_age("Daniel",24)


print(name2)
print(name)
print(age)
print(age2)