import math

def guess_two_missing_numbers(n, S, T):  # O(log n)?
    count1 = n * (n+1) / 2
    count2 = n * (n+1) * (2*n+1) / 6
    
    apb = count1 - S  # a+b
    a2pa2b = count2 - T  # a^2+b^2
    ab = (apb*apb - a2pa2b) / 2  # ab

    amb2 = a2pa2b - 2 * ab

    amb = amb2 ** 0.5
    
    a = (apb + amb) / 2
    b = apb - a

    if a > b:
        b, a = int(a), int(b)
    else:
        a, b = int(a), int(b)

    return a, b

n = int(input())
S, T = [int(x) for x in input().split()]
a, b = guess_two_missing_numbers(n, S, T)
print(a, b)
