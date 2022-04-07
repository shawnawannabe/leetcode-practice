def findDuplicate(a):
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1


a = [1, 2, 3, 2]
findDuplicate(a)
