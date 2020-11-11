import random, timeit
global Qc, Qs, Mc, Ms, Hc, Hs
Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0
##
## 여기에 세 가지 정렬함수를 위한 코드를...
##
def quick_sort(A, first, last):
    global Qc, Qs
    if first >= last:
        return
    left, right = first+1, last
    pivot = A[first]
    while left <= right:
        while left <= last and A[left] < pivot:
            left += 1
            Qc += 1
        while right > first and A[right] >= pivot:
            right -= 1
            Qc += 1
        if left <= right: # swap A[left] and A[right]
            A[left], A[right] = A[right], A[left]
            Qs += 1
            left += 1
            right -= 1
# place pivot at the right place
    A[first], A[right] = A[right], A[first]
    Qs += 1
    quick_sort(A, first, right-1)
    quick_sort(A, right+1, last)


def quick_sort_not_inplace(A):
    if len(A) <= 1:
        return A
    pivot = A[0]
    S, M, L = [], [], []
    for x in A:
        if x < pivot:
            S.append(x)
        elif x > pivot:
            L.append(x)
        else:
            M.append(x)
    return quick_sort_not_inplace(S) + M + quick_sort_not_inplace(L)


def merge_two_sorted_list(A, first, last):
    global Mc, Ms
    m = (first + last) // 2
    i, j = first, m + 1
    B = []
    while i <= m and j <= last:
        Mc += 1
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1
    for k in range(i, m + 1):
        B.append(A[k])
    for k in range(j, last + 1):
        B.append(A[k])
    for i in range(first, last + 1):
        A[i] = B[i - first]
        Ms += 2 * (last - first + 1)

def merge_sort(A, first, last):
    global Mc, Ms
    if first >= last:
        return
    merge_sort(A, first, (first+last)//2)
    merge_sort(A, (first+last)//2 + 1, last)
    merge_two_sorted_list(A, first, last)

def heapify_down(A, k, n):
    global Hc, Hs
    while 2*k+1 < n:
        L, R = 2*k + 1, 2*k + 2
        if L < n and A[L] > A[k]:
            Hc += 1
            m = L
        else:
            Hc += 1
            m = k
        if R < n and A[R] > A[m]:
            Hc += 1
            m = R
        if m != k:
            A[k], A[m] = A[m], A[k]
            Hs += 1
            k = m
        else:
            break

def make_heap(A):
    n = len(A)
    for k in range(n - 1, -1, -1): # A[n-1]→...→A[0]
        heapify_down(A, k, n)


def heap_sort(A):
    make_heap(A)
    global Hs, Hc
    length = A.__len__()
    for k in range(len(A) - 1, -1, -1):
        A[0], A[k] = A[k], A[0]
        length -= 1
        heapify_down(A, 0, length)
        Hs += 1
    return A


# 아래 코드는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
#

def check_sorted(A):
    for i in range(n - 1):
        if A[i] > A[i + 1]: return False
    return True


#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
#


n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000, 1000))
B = A[:]
C = A[:]
print("n =", n)
print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))
print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert (check_sorted(A))
assert (check_sorted(B))
assert (check_sorted(C))
