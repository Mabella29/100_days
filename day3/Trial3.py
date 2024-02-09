#BMI calculator
weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in m:"))

bmi = round(weight / (height * height))

if bmi < 18.5:
    print("you are underweight")
elif 18.5 <= bmi < 25:
    print("you have a normal weight")
elif 25 <= bmi < 30:
    print("you are overweight")
elif 30 <= bmi < 35:
    print("you are obese")
else:
    print("you are clinically obese")