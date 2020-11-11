def reconstruct(S, L):
    result = [None] * len(S)
    for i in range(0, len(S)):
        result[i] = (len(S) - 1 - i) - L[i] + S[i]
    return result

S = [int(x) for x in input().split()] # S[i]는 S[0] 부터 S[i-1]까지 중에 나보다 작은 것의 개수
L = [int(x) for x in input().split()] # L[i]는 L[i+1] 부터 L[-1]까지 중에 나보다 큰 것의 개수
A = reconstruct(S, L)
print(A)
