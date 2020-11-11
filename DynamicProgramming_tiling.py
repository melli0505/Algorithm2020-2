n = int(input())

A = []
B = []
A.append(0)
A.append(1)
A.append(2)
A.append(3)
B.append(0)
B.append(0)
B.append(0)
B.append(2)
for i in range(4, n+1):
    A.append(A[i - 2] + A[i - 1])
    # print(A)
    B.append((A[i - 3] + B[i - 3] + B[i - 1]) * 2 - B[i - 3])
    # print(B)

print(A[n] + B[n])