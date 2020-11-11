def fibo(n):
    count = 0
    first = 0
    second = 1
    while count < n:
        second = first + second
        first = second - first
        count += 1
    return second


n = int(input())
print(fibo(n))