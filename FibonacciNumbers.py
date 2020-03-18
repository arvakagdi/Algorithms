'''
Fibonacci using Dictionary with 2n+2 complexity
'''

def fib(n,fibdic):

    if n <= 1:
        fibdic.update({n: n})
        return n

    else:

        if n not in fibdic:
            result = fib(n-1, fibdic) + fib(n-2, fibdic)
            fibdic.update({n: result})
        else:
            result = fibdic[n]
        return result

f = {}
print (fib(30, f))
