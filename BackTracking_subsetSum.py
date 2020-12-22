def print_subset(x):
    global count
    print([A[i] for i in range(len(x)) if x[i]])
    count += 1


def subset_sum(k):
    global count  # 해의 개수를 세기 위한 global 변수 count
    v_sum = 0
    isEnd = 10000  # x[i]의 요소가 1인 가장 앞 인덱스 저장
    for i in range(len(x)):
        if x[i] == 1:
            v_sum += A[i]
        if x[i] == 1 and i < isEnd:
            isEnd = i
    if isEnd == len(A) - 1 and count == 0:  # 가장 앞 1이 A의 마지막 인덱스인데 답이 아직 없으면
        print("[]")
    if k == len(A):  # k가 len(A)까지 증가했으면
        if v_sum == S:  # 답이면 출력
            print_subset(x)
    else:  # k가 아직 len(A)가 아니면
        if v_sum + A[k] <= S:  # v_sum에 다음 값을 더했을 때 S보다 작으면
            x[k] = 1  # x의 인덱스 k번째를 1로 변경
            subset_sum(k + 1)  # k+1 호출
        x[k] = 0  # 아니면 x[k] = 0
        subset_sum(k + 1)  # A[k]를 포함하지 않은 채로 A[k+1]로 진행


count = 0
# 아래 코드는 수정하지 말고 그대로 사용할 것
A = list(set(int(x) for x in input().split()))
A.sort()
S = int(input())
x = [0] * len(A)
subset_sum(0)