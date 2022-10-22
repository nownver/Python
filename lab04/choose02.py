from decimal import Decimal
import ast

num_input = ast.literal_eval(input("Enter a number: "))

answer = ''
def real_number():
    if type(num_input) is int:
        ask_integer = input("Do you want number in binary, octal, hexadecimal, or decimal?")
        if ask_integer == 'binary':
            binary = bin(num_input)
            answer = str(binary)
        elif ask_integer == 'octal':
            octal = oct(num_input)
            answer = str(octal)
        elif ask_integer == 'hexadecimal':
            hexa = hex(num_input)
            answer = str(hexa)
        elif ask_integer == 'decimal':
            deci = num_input
            answer = str(deci)

    if type(num_input) is float:
        choose_input = input("Do you want to display the number in a floating point or scientific format?")
        if choose_input == 'floating':
            answer = float(num_input)
        elif choose_input == 'scientific':
            answer = '%.2E' % Decimal(num_input)
    return answer

print(real_number())

