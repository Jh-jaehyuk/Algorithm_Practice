def fibo_recursive(x): # 재귀함수를 이용한 정의.
    # 시간복잡도가 O(2**N)으로 매우 비효율적임.
    if x == 1 or x == 2:
        return 1
    return fibo_recursive(x - 1) + fibo_recursive(x - 2)

d = [0] * 100

def fibo(x): # 탑다운(메모이제이션) 이용
    # 시간복잡도가 O(N)으로 매우 효율적임.
    # 종료 조건 (1 혹은 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

# 보텀업 이용 >> 반복문을 이용하여 코드 작성.
# d[1] = 1
# d[2] = 1
# n = 99
# for i in range(3, n + 1):
#     d[i] = d[i - 1] + d[i - 2]
# print(d[n])

print(fibo(99))
