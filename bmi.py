print("This program calculater your body mass index")

height = float(input("Please enter your height in meters: "))
weight = float(input("Please enter how much you weight in kg: "))

bmi = weight /(height ** 2)

print("Your BMI is: ", round(bmi,2))


if (bmi <= 18.5):
    classification = "Underweight"
elif(bmi > 18.5 or bmi <= 24.9):
    classification = "Normal weight"
elif(bmj > 24.9 or bmi <= 29.9):
    classification = "Overweight"
else:
    classification = "Obesity"

print("The classification of your BMI is:", classification)

               
