def find_median_five(L):
    temp3 = L[4]
    if L[0] > L[1]:
        t1 = L[0]
        temp1 = L[1]
    else:
        t1 = L[1]
        temp1 = L[0]
    if L[2] > L[3]:
        t2 = L[2]
        temp2 = L[3]
    else:
        t2 = L[3]
        temp2 = L[2]
    if t2 < temp3:
        tmp = t2
        t2 = temp3
        temp3 = tmp
    if t1 > t2 and temp1 > t2:
        tmp2 = t2
        t2 = temp1
        temp1 = tmp2
    if t1 < t2 and temp3 > t1:
        tmp3 = t1
        t1 = temp3
        temp3 = tmp3

    if temp1 > temp2:
        if temp1 > temp3:
            return temp1
        else:
            return temp3
    else:
        if temp2 > temp3:
            return temp2
        else:
            return temp3


def find_median_unk(L):
    length = len(L)
    if length == 1 or length == 2:
        return L[0]
    if length == 3:
        if L[0] > L[1]:
            if L[0] > L[2]:
                return L[2]
            else:
                return L[0]
        else:
            if L[1] > L[2]:
                return L[2]
            else:
                return L[1]
    else:
        a, b = 0, 0
        if L[0] > L[1]:
            a = L[0]
        else:
            a = L[1]
        if L[2] > L[3]:
            b = L[2]
        else:
            b = L[3]
        if a > b:
            return b
        else:
            return a


    # 5개 값 중 중간값 return

def MoM(L, k): # L의 값 중에서 k번째로 작은 수 리턴
    if len(L) == 1:
        return L[0]
    i = 0
    A, B, M, medians = [], [], [], []
    while i+4 < len(L):
        medians.append(find_median_five(L[i:i+5]))
        i += 5
    if i < len(L) and i+4 >= len(L): #남은 게 1, 2, 3, 4 중에 있으면
        medians.append(find_median_unk(L[i:len(L)]))

    mom = MoM(medians, len(medians)//2)
    for v in L:
        if v < mom: A.append(v)
        elif v > mom: B.append(v)
        else: M.append(v)

    if len(A) >= k:
        return MoM(A, k) # 8
    elif len(A) + len(M) < k:
        return MoM(B, k - (len(A)+len(M)))
    else: return mom

n , k = input().split()
n = int(n)
k = int(k)
print(k)
A = list(map(int, input().split()))
print(MoM(A, k))

#0 3 1 23 34 78 8 -26 32 43 68 91 36 28 35 18 78 71