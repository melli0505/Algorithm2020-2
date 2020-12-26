from operator import itemgetter

def fractional_knapsack(n, size, profit, K):    
    # n개의 아이템, 크기 size[], 가치 profit[], 배낭의 현재 빈 공간 K
    if K <= 0:
        return 0
    s, p = 0, 0
    for i in range(n):
        if s + size[i] <= K: # 배낭에 쏙 들어가면 전체 선택
            p += profit[i]
            s += size[i]
        else: # 넘치면 잘라서 선택
            p += (K-s) * (profit[i]/size[i])
            s = K
            break
    return p

def Knapsack(i, k):  # x[i] = 1인 경우와 0인 경우를 각각 시도함
    global MP
    if i >= n or k <= 0:
        # print(x)
        return x
    p = sum(P[j] for j in range(0, i) if x[j] == 1)
    s = sum(S[j] for j in range(0, i) if x[j] == 1)

    if S[i] <= k:
        B = fractional_knapsack(n-i-1, S[i+1:], P[i+1:], k - S[i])
        if p + P[i] + B > MP:
            if p + P[i] > MP:
                MP = p + P[i]
            x[i] = 1
            Knapsack(i+1, k - S[i])
    x[i] = 0
    B = fractional_knapsack(n-i-1, S[i+1:], P[i+1:], k)
    if p + B > MP:
        x[i] = 0
        Knapsack(i+1, k)


MP = 0
k = int(input()) # 가방 크기
n = int(input()) # 물건 개수
S = list(map(int, input().split())) # 크기
P = list(map(int, input().split())) # 가치
x = [0 for o in range(n)]
SP = []
temp = []
for i in range(n):
    temp.append(S[i])
    temp.append(P[i])
    temp.append(P[i] / S[i])
    SP.append(temp)
    temp = []

SP.sort(key=itemgetter(2), reverse=True)
# print(SP)
for j in range(n):
    SP[j].pop()
# print(SP)

S = []
P = []
for m in range(n):
    S.append(SP[m][0])
    P.append(SP[m][1])
del(SP)

# Knapsack(0, k)
print(fractional_knapsack(n, S, P, k))

# print(MP)