height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = int(weight) / (float(height) ** 2)
print("Your BMI is:", round(bmi))

print("Your BMI is:", round(bmi, 2))