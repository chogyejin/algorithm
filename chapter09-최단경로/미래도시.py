# 259p 예제 9-2 미래 도시
# 전체 회사 N, 경로 수 M(1 <= N, M <= 100), X번 회사 방문 판매, K번 회사 소개팅
# 1번 회사에서 K번 회사 거쳐 X번 회사로 가는 최소 이동 시간 출력하기 
# 1번째 줄 N, M 입력, 2번째 줄 ~ M + 1번째 줄에 연결된 두 회사 번호 입력
# M + 2번째 줄에 X, K(1<= K <= 100) 입력

# 회사(노드) 개수, 경로(간선) 개수
n, m = map(int, input().split())

INF = int(1e9) # 무한

# 2차원 리스트 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자신에서 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0

# 각 간선에 대한 정보 입력 받기, 그 값으로 초기화
for _ in range(m):
  # A와 B가 서로에게 가는 비용은 1이라고 설정
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

# 거쳐 갈 노드 X, 최종 노드 K를 입력받기
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 이용
for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

# 도달 불가 -1 출력
if distance >= 1e9:
  print("-1")
# 도달 가능 시 최소 이동 시간 출력 
else:
  print(distance)

# N 범위가 1 ~ 100이므로 플로이드 워셜로 해결 가능
# 그림을 먼저 그려보자