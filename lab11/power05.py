def power(s):
    result = [[]]
    for i in s:
        result += [x +[i] for x in result]
    for i in range (len(result)):
        result[i] = frozenset(result[i])
    print( set(result))

s = set([1,2,3])
power(s)