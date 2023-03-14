def solution(s):
    s = [int(i) for i in s]
    answer = s[0]
    if len(s) == 1:
        return s[0]
    else:
        for i in range(1, len(s)):
            print(answer)
            if s[i] <= 1 or s[i-1] <= 1:
                answer += s[i]
            else:
                answer *= s[i]
    return answer

print(solution('567'))
