user_weight = input("Weight: ")
float(user_weight)

weight_unit = input("(K)g or (L)bs: ")

if weight_unit == 'K' or weight_unit == 'k':
    final_weight = float(user_weight) * 2.205
    print("Weight in Pounds: ", final_weight)

elif weight_unit == 'L' or weight_unit == 'l':
    final_weight = float(user_weight) / 2.205
    print("Weight in Kgs: ", final_weight)

else:
    print("Invalid weight unit")
