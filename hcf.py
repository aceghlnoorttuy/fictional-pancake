def hcf (*argv):
    import math
    m = []
    for arg in argv:
        n = []
        for i in range (1, arg+1):
            if arg % i == 0:
                n.append(i)
        m.append(n)
    s = set (m[0])
    for i in range (1, len(m)):
        s = s.intersection(set(m[i]))
    l = list(s)
    return max(s)

print(hcf (4, 8, 7))
print(hcf (12, 24, 48))


