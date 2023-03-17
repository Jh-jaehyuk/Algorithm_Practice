# 에라토스테네스의 체 알고리즘의 시간 복잡도는 O(NloglogN)이므로 사실상 선현 시간에 가까울 정도로 매우 빠름.
# 다수의 소수를 찾아야 하는 문제에서 효과적.
# 각 자연수에 대한 소수 여부를 저장해야 하므로 메모리가 많이 필요함.
import math

n = 1000
array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for i in range(2, n + 1):
    if array[i]:
        print(i, end=' ')
