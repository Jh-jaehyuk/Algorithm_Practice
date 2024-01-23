import heapq

# 노드의 개수 입력 받기
v = int(input())

# 각 노드에 연결된 간선 정보를 담기 위한 인접 행렬 입력받기
graph = [list(map(int, input().split())) for _ in range(v + 1)]


def prim(node):
	queue = []
	
	# 각 노드의 방문 여부를 확인하기 위한 배열 만들기
	visited = [0] * (v + 1)
	
	result = 0
	heapq.heappush(queue, (0, node))
	# 큐가 빌 때까지
	while queue:
		dist, now = heapq.heappop(queue)
		
		if not visited[now]: # 방문하지 않은 노드라면
			visited[now] = 1
			result += dist
			
			for i in range(1, v + 1):
				if graph[now][i] and not visited[i]:
					heapq.heappush(queue, (graph[now][i], i))
	
	print(result)
	
	
print(prim(v))
