def pos_tri_num(n):
    if n < 2:
        return n
    else:
        return n + pos_tri_num(n-1)
def sum_tri_num(n):
    if n < 2:
        return n
    else:
        return pos_tri_num(n) + sum_tri_num(n-1)
print(sum_tri_num(5))
