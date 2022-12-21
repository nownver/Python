popularity = {"C++": 93,
              "C": 94,
              "Java": 94,
              "Python": 91,
              "C#": 90}

def rank(dict):
    sorted = list(dict.values())
    sorted.sort()
    sorted.reverse()
    ranking = {}
    spot = 1
    item = list(dict.items())
    # print(item)
    
    for i in range(len(sorted)):
        for k,v in item:
            if sorted[i] == v:
                if (sorted[i] == sorted[i-1]):
                    ranking[spot-1] = ranking[spot-1] + ", " + k
                    spot -= 1
                   
                    break
                else:
                    ranking[spot] = k
        spot += 1

    return ranking

print(rank(popularity))
