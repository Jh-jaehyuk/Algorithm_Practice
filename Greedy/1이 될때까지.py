def solution(N, K):
    answer = 0
    # if N == 1:
    #     return 0
    # while N != 1:
    #     if N % K == 0:
    #         N //= K
    #         answer += 1
    #     else:
    #         N -= 1
    #         answer += 1
    # return answer
    while True: # 시간복잡도가 log(O(N))
        target = (N // K) * K
        answer += (N - target)
        N = target
        if N < K:
            break
        answer += 1
        N //= K

    answer += (N - 1)
    return answer

print(solution(25, 5))
