import functools

@functools.lru_cache(100)
def fib(n):
    """Returns the nth element of the fibonaci sequence"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        x = fib(n-2)
        y = fib(n-1)

        return x + y

def test_fib():
    values = range(0,50)

    fibs = [fib(x) for x in values]
    print(fibs)


test_fib()
