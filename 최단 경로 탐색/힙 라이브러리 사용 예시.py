import heapq

# 최소 힙
# 오름차순 힙 정렬(Heap Sort)
def heapsort_min(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

# 최대 힙
# 내림차순 힙 정렬
def heapsort_max(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result1 = heapsort_min([1,3,5,7,9,2,4,6,8,0])
result2 = heapsort_max([1,3,5,7,9,2,4,6,8,0])
print(result1, result2)
