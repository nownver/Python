sup = set([1,2,3,4])
sub = set([1,2,3])

def is_subset(sub, sup):
    for i in sup:
        for j in sub:
            for a in range(len(sub)):
                if sub(a) not in i:
                    print(False)
                    break
    print(True)
            # if j in i:
            #     print(True)
            # else:
            #     print(False)

# is_subset(sub, sup)



def is_subset(sub, sup):
    c = 0
    sub = list(sub)
    sup = list(sup)
    for i in range (len(sub)):
        if sub[i] not in sup:
            c += 1
            print(False)
            break
    if c == 0:
        print(True)
    

is_subset(sub, sup)