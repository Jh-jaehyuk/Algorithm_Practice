# 위상 정렬 알고리즘의 시간 복잡도는 O(V+E).

# 노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입 차수는 0으로 초기화
visited = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]
# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # 정점 A에서 B로 이동 가능
    
# 위상 정렬 결과 저장할 배열 만들기
result = []

# DFS를 이용한 위상 정렬 함수
def DFS(int node):
	if visited[node]: # 이미 방문한 노드라면 종료
		return
	
	visited[node] = 1 # 노드 방문처리 하기
	
	for i in graph[node]:
		if not visited[i]:
			DFS(i)
			
	result.append(node)
	

DFS(1)
# 배열에 남긴 순서의 역순이 위상정렬 순서이기 때문에 뒤집어주기
for i in reversed(result):
	print(i, end=" ")
