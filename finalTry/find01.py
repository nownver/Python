def find_word_position(s, lst):
    s = s.lower()
    count = []
    for i in range(len(lst)):
        if s == lst[i].lower():
            count.append(i)
    if len(count) == 0:
        return 0
    return count

sam1 = find_word_position("Python", ["python", "java", "c", "PYTHON", "Prolog"])
sam2 = find_word_position("IOS", ["Window", "mac"])
print(sam2)
