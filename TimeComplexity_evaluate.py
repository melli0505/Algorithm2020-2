import time, random

# code for O(n^2)-time function
def evaluate_n2(A, x):
    sum = 0     # 최종 함수 결과값
    nx = 1      # 중간 x값의 제곱 계산
    for i in range(1, len(A)+1):    #함수 계산
        for a in range(1, i):       # x 제곱값 계산
            nx *= x
        sum += A[i-1] * nx
        nx = 1
    return sum

# code for O(n)-time function
def evaluate_n(A, x):
    sum = 0     # 최종 함수 결과값
    count = 1   # 곱할 x값을 저장할 곳
    for i in A:
        sum += i * count
        count *= x
    return sum


random.seed()  # random 함수 초기화
n = int(input())    # n 입력받음
A = []

for i in range(0, n):   # 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움
    A.append(random.randint(-999, 999))

x = random.randint(-99, 99)

# python version 3.8에서는 time.clock()을 지원하지 않아 부득이하게 time.perf_counter()로 대체하였습니다.

# evaluate_n2 호출
begin1 = time.perf_counter()
# print(evaluate_n2(A, x))
# evaluate_n2 수행시간 출력
print(time.perf_counter() - begin1)

# evaluate_n 호출
begin2 = time.perf_counter()
# print(evaluate_n(A, x))
# evaluate_n 수행시간 출력
print(time.perf_counter() - begin2)
