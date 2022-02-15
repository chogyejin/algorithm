# 300p 예제 10-3 도시 분할 계획
# 집 개수 N, 길 개수 M, 다음 줄부터 A번 집, B번 집, C 유지비
# 2개의 마을로 분할하여 유지비 합 최소가 되게 
# 조건 만족하게 길 없애고 유지비 합의 최솟값 출력

# 노드, 간선, 부모 테이블 초기화
v, e = map(int, input().split())
parent = [0] * (v + 1)
for i in range(1, v + 1):
  parent[i] = i

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a < b:
    parent[b] = a
  else: 
    parent[a] = b

edges= [] # 간선 리스트
result = 0 # 최종 비용

for _ in range(e):
  a, b, cost = map(int, input().split()) # A, B, C
  edges.append((cost, a, b)) # tuple

edges.sort()
biggest_edge_cost = 0 # 비용이 가장 큰 간선의 비용

for edge in edges:
  cost, a, b = edge

  # no cycle
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost
    biggest_edge_cost = cost

print(result - biggest_edge_cost)
  
# 최소 신장 트리
# 트리에서 1. 사이클이 없고
# 2. 비용이 가장 큰 간선 제거하면 2개의 부분 그래프로 나뉘어짐