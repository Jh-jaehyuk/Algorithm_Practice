n, k = map(int, input().split()) # n과 k 입력받기
array_A = list(map(int, input().split())) # 배열 A의 모든 원소를 입력받기
array_B = list(map(int, input().split())) # 배열 B의 모든 원소를 입력받기

array_A.sort() # 배열 A는 오름차순 정렬
array_B.sort(reverse=True) # 배열 B는 내림차순 정렬

# 첫번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    # A의 원소가 B보다 작은 경우
    if array_A[i] < array_B[i]:
        # 두 원소를 교체
        array_A[i], array_B[i] = array_B[i], array_A[i]
    else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문 탈출
        break

print(sum(array_A)) # 배열 A의 모든 원소 합을 출력
