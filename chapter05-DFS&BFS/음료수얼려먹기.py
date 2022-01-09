# N X M 얼음칸, 1은 벽
# 0끼리 상하좌우 붙은 아이스크림 개수 출력

n, m = map(int, input().split())

# 2차원 array
data = []
for i in range(n):
  data.append(list(map(int,input()))) # 행마다 쭉 이어서 입력

def count_icecream(x,y):
  # 데이터 바깥 예외처리
  if x < 0 or y < 0 or x >= n or y >= m:
    return False

  #방문하지 않은 노드
  if data[x][y] == 0:
    data[x][y] = 1
    #상하좌우 재귀
    count_icecream(x - 1, y)
    count_icecream(x + 1, y)
    count_icecream(x, y - 1)
    count_icecream(x, y + 1)
    return True

  # 방문했다면 false   
  return False

count = 0
# (0, 0)부터 방문 시작
for i in range(n):
  for j in range(m):
    if count_icecream(i, j) == True:
      count += 1

print(count)

# 이어진 부분들을 재귀적으로 방문해서 찾는 DFS
# DFS 시작 > 예외 > 처음 방문 or 이미 방문
# 1. 처음 방문 > 방문처리 > DFS 반복 >
# 본인 노드에서 연결된 곳 1로 만들고 True 반환하면서 count += 1
# 2. 이미 방문 > False