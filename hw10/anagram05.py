def isAnagram(s1,s2):
    l1 = [i for i in s1]
    l2 = [i for i in s2]
    l1.sort()
    l2.sort()
    if l1 == l2:
        return True
    else:
        return False

print(isAnagram("listen", "silent"))