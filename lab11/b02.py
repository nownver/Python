
# myDict = {'a':'1', 'b':'2','c':'1','d':'3', 'e':'1', 'f':'2'}
# # # a_lst = []
# def find_dup(myDict):
# #     # for i in myDict:
# #     #     for j in myDict:
# #     #         if i ==j:
# #     #             lst.append(i)
# #     # a_list = []
# #     # flipped = {}

# #     # for key, value in myDict.items():
# #     #     if value not in flipped:
# #     #         flipped[value] = [key]
# #     #     else:
# #     #         flipped[value].append(key)

#     reverse_dict = {}
#     for key, value in myDict.items():
#         try:reverse_dict[value].append(key)
#         except:reverse_dict[value] = [key]

#     new = reverse_dict
#     # for i in reverse_dict.copy():
#     #     if len(reverse_dict.get(i)) == 1:
#     #         new.pop(i)

#     # for i in new.copy():
#     #     for j in i.keys():
#     #         print()
#     print(new)

# find_dup(myDict)


# # def find_duplicates(dict):
# #     list1 = list(dict)
# #     list2 = list(dict.values())
# #     newdict = {}
# #     for i in range (len(list2)):
# #         if list2.count(list2[i]) > 1:
# #             newdict[list1[i]] = list2[i]
# #     print(newdict)

# # find_duplicates(myDict)


# 63011335 Tawan Lekngam
# Lab11 Q2

def find_duplicate(param: dict[str, str]) -> dict:
    temp: dict[str, set] = dict()
    res: dict[str, str] = dict()
    for k, v in param.items():
        temp.setdefault(v, set()).add(k)
        # print(temp)
    for k, v in temp.items():
        if len(v) > 1:
            for i in v:
                res[i] = k
    # print(sorted(res.items()))
    return dict((sorted(res.items())))


if __name__ == "__main__":
    samp = {'s5301': 'Fred', 's5302': 'Harry',
            's5303': 'John', 's5304': 'Fred', 's5305': 'Harry'}
    print(find_duplicate(samp))
