# Takes O(n) time
# Takes O(n) memory

F_n = {0: 0, 1: 1}  # F_0 = 0 and F_1 = 1

def fib(n):
    if n in F_n.keys():
        return F_n[n]
    else:
        F_n[n] = fib(n-1) + fib(n-2)
        return F_n[n]
