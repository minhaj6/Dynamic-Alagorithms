# The time complexity increases exponentially,
# while it takes constant memory (only stack)

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


