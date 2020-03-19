'''
GCD using Euclidian Algorithm
'''

def gcd(a, b):
    assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9

    if b == 0:
        return a

    elif a == 0:
        return b

    else:
        if a > b:
            anew = a % b
            if anew != 0:
                return gcd(b, anew)
            else:
                return b
        else:
            bnew = b % a
            if bnew != 0:
                return gcd(a, bnew)
            else:
                return a


print(gcd(28851538, 1183019))
