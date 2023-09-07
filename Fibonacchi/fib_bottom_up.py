# memory usage is very low and constant
# solution time O(n)


def fib(n):
    if n <= 1:
        return n  # returns F_0 = 0 or F_1 = 1

    iteration = 1   # iteration = k-1 
    F_k1 = 1   # F_{k-1}, F_1 as K=2 at first
    F_k2 = 0   # F_{k-2}, F_0 as K=2 at first

    while (iteration < n):  # until iteration = n-1, k=n
        F_k = F_k1 + F_k2
        iteration += 1
        F_k2 = F_k1
        F_k1 = F_k

    return F_k


