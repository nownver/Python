def rank(dct):
    lst = []
    for i in dct:
        lst.append(dct[i])

    lst.sort()
    lst.reverse()
    # print(lst)
    new = dict()
    rank = 1
    #[100, 99.7, 99.7, 97.5, 89.4] 5
    for i in range(len(lst) - 1):
        for k,v in dct.items():
            if lst[i] == lst[i-1]:
                rank -= 1
                break
            if v == lst[i] and lst[i] != lst[i+1]:
                new[rank] = k
                # rank += 1
            elif v == lst[i] and lst[i] == lst[i+1]:
                for a,b in dct.items():
                    if b == lst[i+1]:
                        k2 = a
                        break
                conct =  k + "," + k2
                new[rank] = conct
                print(conct)
        rank += 1

    for k,v in dct.items():   
        if v == lst[len(lst) - 1]:   
            new[rank] = k
    return new




popularity = {"C++": 99.7,
              "C": 99.7,
              "Java": 97.5,
              "Python": 100,
              "C#": 89.4}

a = rank(popularity)
print(a)