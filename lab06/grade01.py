
def grade(score):
    if score <= 100 and score >= 0:
        if score >= 80:
            return 'A'
        elif score >= 70:
            return 'B'
        elif score >= 60:
            return 'C'
        elif score >= 50:
            return 'D'
        else:
            return 'F'

# input_num = int(input("Enter score: "))
g = grade(60)
print(g)
