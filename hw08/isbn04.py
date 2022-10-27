
num_input = input('Enter the first 9 digits of an ISBN-10: ')

last_digit = 0
for i,j in enumerate(num_input):
    last_digit += int(j) * (i+1)
last_digit = last_digit % 11

if num_input.isdigit() and len(num_input) == 9:
    print(f"Your ISBN-10 number is {num_input}{last_digit if last_digit != 10 else 'X'}")