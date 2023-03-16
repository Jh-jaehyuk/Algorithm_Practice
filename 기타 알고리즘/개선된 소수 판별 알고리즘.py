import math
# 소수의 성질을 이용하여 시간 복잡도를 O(X)에서 O(X**0.5)로 줄임.
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
