s1 = set([1, 2, 3])
s2 = set(['p', 'q'])
s3 = set(['a', 'b', 'c'])

def product(*params):
    result = []

    list_params = []
    for i in range(len(params)):
        list_params.append(list(params[i]))
    params = list_params

    for i in range(len(params)):
        if i == 0: #[1,2,3]
            for j in range(len(params[i])):
                result.append([params[i][j]]) # [[1], [2], [3]]
        else:
            temp_result = []
            for j in range(len(result)):
                for k in range(len(params[i])): #['p', 'q']

                    clone_result = (result[j]) #[1],            #[[1,'p']]
                    to_append = params[i][k] #['p],             #['q']
                    clone_result.append(to_append) #[1,'p'],    #[[1,'p','q']]
                    
                    temp_result.append(clone_result) #[[1,'p']] #[[1,'p'], [1,'p','q']]
            result = temp_result #[[1,'p']]
  
    s = set()
    for i in result:
        s.add(tuple(i))
    return s

answer = product(s1, s2, s3)

print(answer)


a = [1,2,3,4]

result = list(a)
# result = a

a.append(0)
print(result)