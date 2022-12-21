myDict = {'a':'1', 'b':'2', 'c':1, 'd':'3'}

def inverse(dict):
    reverse_dict = {}
    for key, value in dict.items():
        try:reverse_dict[value].append(key)
        except:reverse_dict[value] = [key]

    # new = reverse_dict
    # for i in reverse_dict.copy():
    #     if len(reverse_dict.get(i)) == 1:
    #         new.pop(i)

    # # for i in new.copy():
    # #     for j in i.keys():
    # #         print()
    # print(new)

    # new = reverse_dict
    # for i in reverse_dict.copy():
    #     if len(reverse_dict.get(i)) == 1:
    #         new.pop(i)

    print(reverse_dict)
inverse(myDict)