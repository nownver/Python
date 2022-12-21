
def composite(dict1, dict2):
    dict3 = {}
    for k,v in dict1.items():
        for i,j in dict2.items():
            if v == i:
                dict3[k] = j

    return dict3

dict1 = {'a':'p', 'b':'r', 'c':'q', 'd':'p', 'e':'s'}
dict2 = {'p': '1', 'q':'2', 'r':'3'}

print(composite(dict1, dict2))      
