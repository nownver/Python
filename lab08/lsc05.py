# dic = []

# def LCS(s1, s2):
#     for i,j in enumerate(s1):
#         for k,l in enumerate(s2):
#             if j == l:
#                 dic.append(j)
#             if 
                
#     return dic

# a = LCS("ingenious", "intelligent")
# print(a)
# s = ""


# def LCS(s1, s2):
#     s = ""
#     for i in s1:
#         if i in s2:
#             # print(i, end ="")
#             s += i
#         if s not in s1 or s not in s2:
#             # s = s[:len(s2)-1]
#             break
#     return s
    
# a = LCS("ingenious", "intelligent")
# print(a)

# s = "yok"
# if s.iscontains

# def check(s1,s2):
#     ans = ""
#     if len(s1) > len(s2):
#         for i in s1:
#             if i in s2:
#                 continue
#             else:
#                 ans = "" + i
#     else:
#         for i in s2:
#             if i in s1:
#                 continue
#             else:
#                 ans = "" + i
#     return ans


# def LCS(s1, s2):
#     dic = []
#     s = ""
#     for i in s1:
#         for j in s2:
#             if i == j:
#                 # dic.append(j)   
#                 s += i
#     return s

# a = LCS("ingenious", "intelligent")
# print(a)
# s = ""

# def lcs(s1, s2):
#     s = ""
#     for i in s1:
#         for j in s2:
#             if i in s2 and j in s1:
#                 s += i
#                 if s not in s1 or s not in s2:
#                     s = s[0:len(s)-1]
#                 # s = s[0:len(s)-1]
#     return s
 

# b = lcs("ingenious", "intelligent")
# print(b)

# def lcs(s1, s2):
#     s2_len = len(s2)
#     for i,v in enumerate(s1):
#         s2 = s1[i:s2_len+i]
#         if s1 == s2:
#             return s1

# b = lcs("ingenious", "intelligent")
# print(b)

# dic = []
# def LCS(s1, s2):
#     for i,j in enumerate(s1):
#         for k,l in enumerate(s2):
#             if j == l:
#                 dic.append(j)
#             if 
#                 # 
#     return dic

# a = LCS("ingenious", "intelligent")
# print(a)
# s = ""


# s1 = input("s1: ")
# s2 = input("s2: ")

# def LCS(s1, s2):
#     max = 0
#     common = ""
#     result = ""
#     for i in s1:
#         if i in s2:
#             common += i
#             if common not in s2:
#                 length = len(common)
#                 if length > max :
#                     result = common[:-1]
#                     max = length
#                 result = common
                
#             common = i
#         print(i)
#         print(common)
#     print(result)


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

#abc_de, de_abc_fg -> abc
# def lcs(s1, s2):
#     for i in s1:
#         for j in s2:
#            if i == j:


def check(s1, s2):
    c = 0
    for i in range(len(s2)):
        sub = s2[i:len(s1) + i]
        if sub == s1:
            c = 1
            return True
    if c == 0:
        return False

# ans = check("ura", "naura")
# print(ans)

def lcs(s1, s2):
    s = ""
    c = 0
    l = []
    ls = []
    max = 0
    ans = ""
    # max_i = 0
    max_i = 0
    for i in range(len(s1)) :
        for j in range(len(s1)+1) :
            if(s1[i:j] != "") :
                # l.append(s1[i:j])
                s = s1[i:j]
    # print(l)
            if check(s, s2) == True:
                c = 1
                l.append(s)

            # print(s)
    if c == 0:
        return False
    for i in l:
        len_s = len(i)
        ls.append(len_s)
    for i,j in enumerate(ls):
        if j >= max:
            max = j
            max_i = i         
        ans = l[max_i]
    # print(l)
    return ans

ans = lcs("metaverse", "universe")
print(ans)

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
