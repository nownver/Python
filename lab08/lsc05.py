l = []
def LCS(s1, s2):
    max = ""
    for i in range(len(s1)):
        for j in range(len(s1) + 1):
            if s1[i:j] in s2:
                l.append(s1[i:j])
                if len(s1[i:j]) >= len(max):
                    max = s1[i:j]
    print(max)

LCS("philosophically","zoophilous")
LCS("multiverse", "metaverse")
LCS("scada", "kmitl")
LCS("interactive", "inaction")
LCS("ingenious","intelligent")
LCS("pen","pen pineapple apple pen")
LCS("abcdef","cde")


# s1 = input("s1: ")
# s2 = input("s2: ")

# def LCS(s1, s2):
#     max = 0
#     common = ''
#     result = ''
#     for i in s1:
#         if i in s2:
#             common += i
#             result = common
#             if common not in s2:
#                 length = len(common)
#                 if length > max :
#                     result = common[:-1]
#                     max = length
#                 common = i
#         # print(i)
#         # print(common)
#         # print(result)
#     print(result)

# LCS(s1, s2)


# def check(s1, s2):
#     c = 0
#     for i in range(len(s2)):
#         sub = s2[i:len(s1) + i]
#         if sub == s1:
#             c = 1
#             return True
#     if c == 0:
#         return False

# ans = check("ura", "naura")
# print(ans)
# def lcs(s1, s2):
#     s = ""
#     c = 0
#     l = []
#     ls = []
#     max = 0
#     ans = ""
#     # max_i = 0
#     max_i = 0
#     for i in range(len(s1)) :
#         for j in range(len(s1)+1) :
#             if(s1[i:j] != "") :
#                 # l.append(s1[i:j])
#                 s = s1[i:j]
#     # print(l)
#             if check(s, s2) == True:
#                 c = 1
#                 l.append(s)

#             # print(s)
#     if c == 0:
#         return False
#     for i in l:
#         len_s = len(i)
#         ls.append(len_s)
#     for i,j in enumerate(ls):
#         if j >= max:
#             max = j
#             max_i = i         
#         ans = l[max_i]
#     # print(l)
#     return ans

# ans = lcs("metaverse", "universe")
# print(ans)

# 1234 -> 
# 1 
# 12, 123, 1234
# 2
# 23 234
# 3
# 34
# 4

# a = "1234"
# s = ""
# ml = []

# for i in range(len(a)) :
#     for j in range(len(a)+1) :
#         if(a[i:j] != "") :
#             ml.append(a[i:j])
# print(ml)

# a = "1234"
# a = a[2:1]
# print(a)

#ml = []
# for i in range(len(a)):
#     for j in range(len(a) + 1):
#         ml.append(a[i:j])

# print(ml)

