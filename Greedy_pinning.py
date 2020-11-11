# def quick_sort_not_inplace(A):
#     if len(A) <= 1:
#         return A
#     pivot = A[0][1]
#     S, M, L = [], [], []
#     for x in range(len(A)):
#         p = A[x][1]
#         if p > pivot:
#             S.append(A[x])
#         elif p < pivot:
#             L.append(A[x])
#         else:
#             M.append(A[x])
#     return quick_sort_not_inplace(S) + M + quick_sort_not_inplace(L)

# def heapify_down(A, k, n):
#     while 2*k+1 < n:
#         L, R = 2*k + 1, 2*k + 2
#         if L < n and A[L][1] < A[k][1]: # < >
#             m = L
#         else:
#             m = k
#         if R < n and A[R][1] < A[m][1]: # < >
#             m = R
#         if m != k:
#             A[k], A[m] = A[m], A[k]
#             k = m
#         else:
#             break
#
# def make_heap(A):
#     n = len(A)
#     for k in range(n - 1, -1, -1): # A[n-1]→...→A[0]
#         heapify_down(A, k, n)
#
#
# def heap_sort(A):
#     make_heap(A)
#     length = A.__len__()
#     for k in range(len(A) - 1, -1, -1):
#         A[0], A[k] = A[k], A[0]
#         length -= 1
#         heapify_down(A, 0, length)
#     return A

from operator import itemgetter
import inspect

def pin(A):
    pin = 1
    lb = A[0]
    for i in range(1, len(A)):
        if lb[0]<= A[i][0] <= lb[1] or lb[0] <= A[i][1] <= lb[1] or A[i][0] <= lb[0] <= lb[1] <= A[i][1]: # 조건 생각해봐
            if lb[0] < A[i][0]:
                lb[0] = A[i][0]
            if lb[1] > A[i][1]:
                lb[1] = A[i][1]
            if lb[0] > lb[1]:
                break
        else:
            lb = A[i]
            pin += 1
    return pin


n = int(input())
A = []
temp = []
for i in range(n):
    temp = list(map(int, input().split()))
    A.append(temp)
    # print(A)
    # A[i].append(A[i][1] - A[i][0])
    temp = []

# sortedA = heap_sort(A)
# inspect.getsource(sorted)
A.sort(key=itemgetter(1), reverse=True)
# print(A)
# print(pin(A))
