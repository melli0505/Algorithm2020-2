def reconstruct(B):
    A = []
    num_list, num_bool = [], []
    A.append(B[-1])
    for i in range(0, len(B)):
        num_list.append(i)
        # num_bool.append(False)
        i += 1
    # num_bool[A[0]+1] = True

    num_list.pop(B[-1])
    j = len(B)-2
    while j > -1:
        A.insert(0, num_list[B[j]])
        num_list.pop(B[j])
        j -= 1

    return A


B = [int(x) for x in input().split()]
A = reconstruct(B)
print(A)
