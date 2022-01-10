# 152p 예제 5-4 미로 탈출
# N X M 미로에서 (1, 1) > (N, M) 출구 최소 비용
# 0은 벽, 1은 갈 수 있는 길

from collections import deque

n, m = map(int,input().split())

data = []
for i in range(n):
  data.append(list(map(int,input())))

move_x = [-1, 0, 0, 1] #상 좌 우 하
move_y = [0, -1, 1, 0]

def escape_maze(x, y):
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      temp_x = x + move_x[i]
      temp_y = y + move_y[i]
      
      # 예외(맵 밖, 벽)
      if (temp_x < 0 or temp_y < 0 or temp_x >= n or temp_y >= m) or (data[temp_x][temp_y] == 0):
        continue
      
      if data[temp_x][temp_y] == 1:
        data[temp_x][temp_y] = data[x][y] + 1
        queue.append((temp_x, temp_y))
  
  return data[n - 1][m - 1] # (N, M) 좌표의 노드 값 리턴

count = escape_maze(0, 0)
print(count)

# 가까운 곳부터 탐색하는 BFS
# 큐 생성 > 상좌우하 temp, 예외 처리 > 
# 갈 수 있으면 탐색하러 갈 곳 = 현재 노드 값 + 1 > 큐에 추가 