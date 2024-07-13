# This file is for control flow (conditions)

temperature = 35


# indentation is important (same as curly brackets)
if temperature > 35:
    print("Its a hot day")
elif temperature < 35:
    print("Its a cold day")

print("Temperature check is done")



# Weight converter



weight = float(input("Whats your weight: "))
unit = input("(K) for kg  or (L) for lbs: ")
weight_value = 0.00;

if(unit.upper() =="K"): 
    weight_value = weight/0.45
    print("Weight in Kg:", weight_value)
elif (unit.upper() == "L"):
    weight_value = weight * 0.45
    print("Weight in lbs:", weight_value)
else:
     print("Weight unit not found in system")


