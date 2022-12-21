s1 = set([1, 2, 3])
s2 = set(['p', 'q'])
s3 = set(['a', 'b', 'c'])

def product(*params):
    result = []

    list_params = []
    for i in range(len(params)):
        list_params.append(list(params[i]))
    params = list_params
    print(params)

    for i in range(len(params)):
        if i == 0:
            for j in range(len(params[i])):
                result.append([params[i][j]])
        else:
            temp_result = []
            for j in range(len(result)):
                for k in range(len(params[i])):
                    result[j].append(params[i][k])
                    temp_result.append(list(result[j]))
                    result[j].pop()
            result = temp_result

    s = set()
    for i in result:
        s.add(tuple(i))
    return s

answer = product(s1, s2, s3)

print(answer)
