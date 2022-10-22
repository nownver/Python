# def find_grade(score):
#     grade = ''
#     if score > 0 and score <= 100:
#         if score < 50:
#             grade = 'F'
#         elif score < 60:
#             grade = 'D'
#         elif score < 70:
#             grade = 'C'
#         elif score < 80:
#             grade = 'B'
#         else:
#             grade = 'A'
#     else:
#         print("Score must be in range of 0 to 100")
#     return grade

# score_input = int(input("Enter a score: "))
# grade = find_grade(score_input)
# print(f"Your grade: {grade}")

def find_grade(score):
    grade = ''
    if score > 0 and score <= 100:
        if score < 50:
            grade = 'F'
        elif score < 60:
            grade = 'D'
        elif score < 70:
            grade = 'C'
        elif score < 80:
            grade = 'B'
        else:
            grade = 'A'
    else:
        grade = 'Score must be in range of 0 to 100'
    return grade

score_input = int(input("Enter a score: "))
grade = find_grade(score_input)
print(f"Your grade: {grade}")
