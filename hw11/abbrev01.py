abbrv = {'be': 'b',
        'because': 'cuz',
        'see': 'c',
        'the': 'da',
        'okay': 'ok',
        'are': 'r',
        'you': 'u',
        'without': 'w/o',
        'why': 'y',
        'see you': 'cu',
        'ate': '8',
        'great': 'gr8',
        'mate': 'm8',
        'wait': 'w8',
        'later': 'l8r',
        'tomorrow': '2mro',
        'for': '4',
        'before': 'b4',
        'once': '1ce',
        'and': '&',
        'Your': 'ur',
        "You're": 'ur',
        'As far as I know': 'afaik',
        'As soon as possible': 'ASAP',
        'At the moment': 'atm',
        'Be right back': 'brb',
        'By the way': 'btw',
        'For your information': 'FYI',
        'In my humble opinion': 'imho',
        'In my opinion': 'imo',
        'Laughing out loud': 'lol',
        'Oh my god': 'omg',
        'Rolling on the floor laughing': 'rofl',
        'Talk to you later': 'ttyl',
        }

def textese(s):
    s = s.lower()
    lst = s.split()
    tuple_phrase = list(abbrv.items())[22:] 
    tuple_phrase.append(list(abbrv.items())[9])
    tuple_phrase.append(list(abbrv.items())[17])

    for j in tuple_phrase:
        if j[0].lower() in s:
            s = s.replace(j[0].lower(), j[1])

    for k,v in abbrv.items():
        if k.lower() in lst:
            s = s.replace(k.lower(), v)
    
    return s
            
def untextese(s):
    lst = s.split()

    for i in range(len(lst)):
        for k,v in abbrv.items():
            if v.lower() == lst[i].lower():
                lst[i] = k
    
    s_new = ''
    for i in lst:
        s_new += i + ' '

    return s_new

message1 = "for your information because without you see you before ate mate ate for"
message2 = "fyi cuz w/o u cu b4 8 m8 8 4"
       
print(textese(message1))
print(untextese(message2))
