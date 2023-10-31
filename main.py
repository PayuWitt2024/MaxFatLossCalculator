weight = float(input("Enter your weight (kg): "))
bf_p = float(input("Enter your bodyfat percentage: "))
bf_m = 0.01*bf_p*weight
f_bf_p = float(input("Enter your goal bodyfat percentage: "))
day = 0
kcal_def = 0
while bf_p > f_bf_p:
    f_loss = (kcal_def / 3500) * 0.45359237
    weight -= f_loss
    bf_m -= f_loss
    bf_p = (bf_m / weight) * 100
    print("At day {0}, you should have a Calorie deficit of {1:.2f} kcal to attain:\n - a weight of {2:.2f}\n - a bodyfat percentage of {3:.2f}".format(day, kcal_def, weight, bf_p))
    # The daily maximum calorie deficit beyond which muscle atrophy begins to exponentiate is 31 kcal/lb of body fat
    kcal_def = bf_m*2.2046226218*31
    day += 1
