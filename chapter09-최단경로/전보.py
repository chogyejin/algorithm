# C도시에서 메시지 최대한 많이 보냄
# 도시 N개, 통로 M개, C도시 출발, X도시에서 Y도시 시간 Z
# 메시지 받는 도시 개수, 모두 메시지를 받는 데까지 걸리는 시간 출력
# 1 <= N <= 30000, 1 <= M <= 200000, 1 <= C <= N
# 1 <= X,Y <= N, 1 <= Z <= 1000

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


# 도시 개수 N, 통로 개수 M, 보내는 도시 C
n, m, c = map(int, input().split())
# 노드 연결 정보 그래프
graph = [[] for i in range(n + 1)] # 초기화는 0부터 n까지
# 최단 거리 테이블 result
result = [INF] * (n + 1)

# X to Y, cost Z
for _ in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((y, z))

def send_message_from(c):
  q = []
  result[c] = 0
  heapq.heappush(q, (0, c)) # 시작 노드 push

  while q:
    dist, now = heapq.heappop(q)

    if result[now] < dist: # 갱신한 적 있으면 패스
      continue
    
    for i in graph[now]:
      cost = dist + i[1] # i[i]는 그 노드까지의 거리 값
      
      if cost < result[i[0]]: # i[0]는 노드, 갱신이 가능하다면 갱신
        result[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

send_message_from(c)

count = 0 # 후에 시작 노드를 제외하는 -1 수행
total_time = 0 # 다른 노드로 가는 것 중에 제일 긴 시간
for i in result:
  if i != INF: # 도달 가능하면
    count += 1
    total_time = max(total_time, i)
  
print(count - 1, total_time)

# heapq.heapqush(arr, element)
# heapq.heappop(arr)
# graph는 [(node1, cost1), (node2, cost2)...] 형태
# dist(꺼낸 거리 값)가 result[now]보다 작으면 이미 갱신 처리가 된 것