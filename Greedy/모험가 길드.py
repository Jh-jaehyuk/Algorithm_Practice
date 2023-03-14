from collections import Counter
def solution(group):
    group = Counter(group)
    answer = 0
    group = list(group.items())
    print(group)
    for i in range(len(group)):
        if group[i][1] >= group[i][0]:
            answer += 1

    return answer

# n = int(input())
# data = list(map(int, input().split()))
# data.sort()
#
# result = 0
# count = 0
#
# for i in data:
#     count += 1
#     if count >= i:
#         result += 1
#         count = 0
#
# print(result)

print(solution([2,3,1,2,2]))
