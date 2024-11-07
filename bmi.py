heigth = int(input("Enter your height: "))
weight = int(input("Enter your weight: "))
heigth /= 100
bmi = (weight)/(heigth**2)

print(f"BMI is {bmi:.3f}")