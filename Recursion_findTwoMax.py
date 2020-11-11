def two_max(A, left, right):
    if A == []:
        return None, None

    if left == right:
        return A[left], None

    mid = (left + right) // 2

    if left != right:
        A1, A2 = two_max(A[0:mid+1], 0, mid)
        B1, B2 = two_max(A[mid+1:right+1], 0, right-mid-1)

        mm = [A1, A2, B1, B2]
        M = -2147483648
        m = -2147483648
        for i in mm:
            if i is not None and i > M:
                m = M
                M = i
            elif i is not None and M >= i >= m:
                m = i


        if M == -2147483648:
            M = None
        if m == -2147483648:
            m = None

        return M, m

A = list(map(int, input().split()))
M, m = two_max(A, 0, len(A)-1)
print(M, m)

# M = biggest, m = second
# M과 m이 같을 수 있음
# 1. base case
# 2. 재귀적으로 left ... mid 에 대해 가장 큰 값 L1과 L2 계산
# 3. 재귀적으로 mid + 1 ... right에 대해 가장 큰 값 R1과 R2 계산
# 4. L1, L2, R1, R2로부터 left ... right에 대한 M, m 계산
# L2와 R2가 None일 수 있음