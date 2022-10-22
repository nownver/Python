num_input = int(input("Enter number n: "))
temp = 0

def find_sqrt(time):
    guess_sqrt = num_input / 2
    for i in range(time):
        temp = num_input / guess_sqrt
        guess_sqrt = (guess_sqrt + temp) / 2
    return guess_sqrt

five_sqrt = find_sqrt(5)
six_sqrt = find_sqrt(6)
seven_sqrt = find_sqrt(7)

format_five_sqrt = "{:.3f}".format(five_sqrt)
format_six_sqrt = "{:.3f}".format(six_sqrt)
format_seven_sqrt = "{:.3f}".format(seven_sqrt)

print(f"iterate with 5: {format_five_sqrt}")
print(f"iterate with 6: {format_six_sqrt}")
print(f"iterate with 7: {format_seven_sqrt}")

