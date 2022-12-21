s1 = set([1, 2, 3])
s2 = set(['p', 'q'])
s3 = set(['a', 'b', 'c'])

def product(*params):

    param_lst = []
    for i in params:
        param_lst.append(list(i))
    params = param_lst
    print(params)





product(s1, s2)