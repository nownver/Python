name = input("Enter your name: ")
age = input("Enter your age: ")
weight = input("Enter your weight in Kg: ")
height = input("Enter your height in cm: ")

int_age = int(age)
float_weight = float(weight)
float_height = float(height)
height_in_m = float_height / 100.0

bmi = float_weight / (height_in_m) ** 2

def bmi_chart(age, bmi):
    word = ''
    if age < 17:
        if bmi < 15:
            word = 'Underweight'
        elif bmi > 20:
            word = 'Overweight'
        else:
            word = 'normal'
    elif age >= 17 and age <= 35:
        if bmi < 18:
            word = 'Underweight'
        elif bmi > 24:
            word = 'Overweight'
        else:
            word = 'normal'
    elif age > 35:
        if bmi < 19:
            word = 'Underweight'
        elif bmi > 26:
            word = 'Overweight'
        else:
            word = 'normal'
    return word

float_9_bmi = "{:.9f}".format(bmi)
# print(float_9_bmi)
word_bmi = bmi_chart(int_age, bmi)
print(f"Your body mass index (BMI) is {float_9_bmi}")
print(f"{name}, you are {word_bmi}")