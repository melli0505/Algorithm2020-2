W = int(input())
words = input().split()

length = [len(i) for i in words]  # 모든 단어의 길이를 저장하는 배열
wordsLen = [[-1 for x in range(len(words))]for y in range(len(words))]  # W - n부터 m까지의 길이 저장
wordPenalty = [[-1 for x in range(len(words))]for y in range(len(words))]  # n부터 m까지 penalty 저장
# len table
i = 0
for i in range(0, len(words)):
    wordsLen[i][i] = W - len(words[i])
    for j in range(i + 1, len(words)):
        wordsLen[i][j] = wordsLen[i][j - 1] - 1 - len(words[j])
# print(wordsLen)
# penalty table
for o in range(0, len(words)):
    for k in range(o, len(words)):
        if wordsLen[o][k] < 0:
            wordPenalty[o][k] = -1
        else:
            wordPenalty[o][k] = wordsLen[o][k] ** 3
# print(wordPenalty)

optimization = [0] + [2147483647 for i in range(len(words))]
penalty = 2147483647
for b in range(0, len(words)):
    for a in range(b, -1, -1):
        # temp = wordPenalty[a][b]
        if wordPenalty[a][b] == -1:
            penalty = 2147483647
        else:
            penalty = optimization[a] + wordPenalty[a][b]
        if optimization[b+1] > penalty:
            optimization[b+1] = penalty
            penalty = 2147483647
# print(optimization)
print(optimization[-1])



























# penalty = 10000000
# for i in range(0, len(words)):
#     j = i
#     while j >= 0:
#         temp = wordsLen[j][i]
#         if wordsLen[j][i] < 0:
#             penalty = 10000000
#         else:
#             penalty = result[j] + wordPenalty[j][i]
#         if result[i + 1] > penalty:
#             result[i+1] = penalty
#         j -= 1
#
# print(result[-1])




# # 차선책과 최선책 비교
# APenalty = -10
# Atemp = 0
# BPenalty = -10
# Btemp = 0
# CPenalty = -10
# Ctemp = 0
# sum = 0
# l, m, n, p = 0, 0, 0, 0
# locM = 0
# while l < len(words):
#     APenalty = -10
#     Atemp = 0
#     BPenalty = -10
#     Btemp = 0
#     CPenalty = -10
#     Ctemp = 0
#     for m in range(l, len(words)): # 처음 같은 행에서 값 두 개 찾기
#         if wordPenalty[l][m] != -1:
#             CPenalty = BPenalty
#             BPenalty = APenalty
#             APenalty = wordPenalty[l][m]
#         else:
#             m -= 1
#             break
#
#     for n in range(m + 1, len(words)): # 가장 작은 패널티에 연결되는 패널티 찾기
#         if wordPenalty[m+1][n] != -1:
#             Atemp = wordPenalty[m+1][n]
#         else:
#             n -= 1
#             break
#     APenalty += Atemp
#     for p in range(m, len(words)):
#         if wordPenalty[m][p] != -1:
#             Btemp = wordPenalty[m][p]
#         else:
#             p -= 1
#             break
#     BPenalty += Btemp
#     for q in range(m - 1, len(words)):
#         if CPenalty == -10:
#             break
#         if wordPenalty[m - 1][q] != -1:
#             Ctemp = wordPenalty[m - 1][q]
#         else:
#             q -= 1
#             break
#     CPenalty += Ctemp
#     if APenalty > BPenalty:
#         if CPenalty != -10:
#             if BPenalty > CPenalty:
#                 l = q + 1
#                 sum += CPenalty
#                 pic = len(words) - q
#             else:
#                 l = p + 1
#                 sum += BPenalty
#                 pic = len(words) - p
#         else:
#             l = p + 1
#             sum += BPenalty
#             pic = len(words) - p
#     else:
#         if CPenalty != -10:
#             if APenalty > CPenalty:
#                 l = q + 1
#                 sum += CPenalty
#                 pic = len(words) - q
#             else:
#                 l = n + 1
#                 sum += APenalty
#                 pic = len(words) - n
#         else:
#             l = n + 1
#             sum += APenalty
#             pic = len(words) - n
#         # l = n + 1
#         # sum += APenalty
#
#     if pic >= len(words) - 1 or l >= len(words) - 1 or m == len(words) - 1:
#         break
#
#
#

# print(sum)





