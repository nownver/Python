
# list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
# def find_word(l1, l2, n):
#     for i in l1:
#         if int(n) == i:
#             w = l2[i]
#     return w

# def num_teen(num):
#     if num[1] == "1":
#         result = "eleven"
#     elif num[1] == "2":
#         result = "twelve"
#     elif num[1] == "3":
#         result = "thirteen"
#     elif num[1] == "5":
#         result = "fifteen"
#     else:
#         result = num[1] + "teen"
#     return result

# def special_ty(num):
#     if num[0] == "2":
#         if num[0] == "0":
#             result = "twenty"
#         else:
#             result = "twenty" + "-" + num[1]
#     elif num[0] == "3":
#         if num[0] == "0":
#             result = "thirty"
#         else:
#             result = "thirty" + "-" + num[1]
#     elif num[0] == "5":
#         if num[0] == "0":
#             result = "fifty"
#         else:
#             result = "fifty" + "-" + num[1]
#     # elif:
#     #     result = num[0] + "ty" 
#     return result

# def format_num(num):
#     result = ""
#     number = ""
#     num_0 = find_word(list1, list2, num[0])
#     num_1 = find_word(list1, list2, num[1])
#     num_2 = find_word(list1, list2, num[2])

#     if len(num) == 1:
#         result = find_word(list1, list2, num)
#     elif len(num) == 2:
#         if num[0] == 1:
#             result = num_teen(num[1:3])
#         elif num[0] == 2 or num[0] == 3:
#             result = special_ty(num[1:3])
#         elif num[1] == "0":
#             result = num_0 + "ty"
#         else:
#             result = num_0 + "ty" + "-" + num_1
    
        
