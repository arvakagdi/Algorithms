'''
Fibonacci Numbers using List | Iterative solution
'''

def fibonacci_number(n):
    fiblist = []
    fiblist.append(0)
    fiblist.append(1)

    if n <= 1:
        #   fiblist.append(n)
        return n
    else:
        for i in range(2, n + 1):
            result = fiblist[i - 1] + fiblist[i - 2]
            fiblist.append(result)
    return fiblist[n]



print(fibonacci_number(198))


# 0.02/5.00, max memory used: 9146368/536870912.)