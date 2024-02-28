def pos_tri_num(n):
    if n < 2:
        return n
    else:
        return n + pos_tri_num(n-1)
def sum_tri_num(n):
    if n < 2:
        return n
    else:
        return f"The sum of the first {n} triangular numbers is {pos_tri_num(n) + sum_tri_num(n-1)}."
print(sum_tri_num(5))
