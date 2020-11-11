def findleastindex(A, left, right):
    if A == []:
        return None, None

    if left == right:
        return A[left], left

    mid = (left + right) // 2

    if left != right:
        m1, index1 = findleastindex(A, left, mid)
        m2, index2 = findleastindex(A, mid+1, right)
        if m1 > m2:
            M = m2
            index = index2
        else:
            M = m1
            index = index1

        return M, index


A = list(map(int, input().split()))
min, minIndex = findleastindex(A, 0, len(A)-1)

if minIndex == 0:
    result = 0
else:
    result = len(A) - minIndex
print(result)

