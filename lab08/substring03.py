# s1 = input("s1: ")
# s2 = input("s2: ")

# #abcd bc
# s = ''
# a = s1
# b = s2

# if len(s1) > len(s2):
#     a = s2
#     b = s1

# for i in a:
#     # print(i)
#     for j in b:
#         if i == j:
#             s += i
#             # print(f"in {s}")
#             if s not in a:
#                 s = s[:-1]
#             if s not in b:
#                 s = s[:-1]
  
#     # print(s)
# if s == a:
#     print("sub")
# else:
#     print("not")

# print(s)



# s1 = input("s1: ")
# s2 = input("s2: ")

# if s2.__contains__(s1) or s1.__contains__(s2):
#     print("substring")
# else:
#     print("not substring")

###wrong
# def check(s1,s2):
#     ans = "not substring"
#     if len(s1) > len(s2):
#         for i in s1:
#             if i in s2:
#                 continue
#             else:
#                 ans = "substring"
#     else:
#         for i in s2:
#             if i in s1:
#                 continue
#             else:
#                 ans = "substring"
#     return ans

# print(check(s1,s2))

# def check(s1, s2):
#     while


# s2_len = len(s2)
# for i,v in enumerate(s1):
#     s2 = s1[i:s2_len+i]
#     if s1 == s2:
#        print("sub")

# x = 0
# while x < len(s1):
#     s2 = s1[x:len(s2) + x]
#     if s1 == s2:
#         print("sub")
#     else:
#         pass
#     x += 1


# main_string = input("long: ")
# match_string = input("short: ")
        
# len_match_string = len(match_string)
# for index,value in enumerate(main_string):
#     sub_string = main_string[index:len_match_string+index]
#     print(index)
#     print(sub_string)
#     if sub_string == match_string:
#        print("sub")

# x = 0
# match_string_len = len(match_string)
# while x < len(main_string):
#     sub_string = main_string[x:match_string_len + x]
#     if sub_string == match_string:
#         print("sub")
#     x += 1

# fullstring = "StackAbuse"
# substring = "tack"

# if substring in fullstring:
#     print("Found!")
# else:
#     print("Not found!")

# short = s1
# long = s2
# c = 0

# for i in range(len(long)):
#     sub = s2[i:len(short)+i]
#     # print(sub)
#     if short == sub:
#         c += 1
#         print("True")
#         break
# if c == 0:
#     print("False")
   

# short = input("short:")
# long = input("long: ")

# c = 0
# x = 0
# while x < len(long):
#     sub = long[x: len(short) + x]
#     if sub == short:
#         c += 1
#         print("True")
#         break
#     x += 1

# if c == 0:
#     print("False")

# s1 = "ura"
# s2 = "weurawe"
