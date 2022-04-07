def firstUniqueChar(string):
    d = {}
    for i, char in enumerate(string):
        if char not in d:
            d[char] = 1
        elif char in d:
            d[char] += 1
    for key, items in d.items():
        if items == 1:
            return key


stringX = "geeksforgeeks"
firstUniqueChar(stringX)
