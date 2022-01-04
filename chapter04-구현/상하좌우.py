# 110p 예제 4-1 상하좌우
# (1,1) 시작, LRUD 입력받아 최종 좌표 출력

n = int(input())
my_moves = list(input().split())

move_x = [0, 0, -1, 1]
move_y = [-1, 1, 0, 0]
x=1
y=1

for move in my_moves:
  if move=='L':
    x += move_x[0]
    y += move_y[0]
  elif move=='R':
    x += move_x[1]
    y += move_y[1]
  elif move=='U':
    x += move_x[2]
    y += move_y[2]
  elif move=='D':
    x += move_x[3]
    y += move_y[3]
  
  if x < 1:
    x += 1
  if x > n:
    x -= 1
  if y < 1:
    y += 1
  if y > n:
    y -= 1

print(x, y)

# move_list 배열, 임시좌표(nx, ny) 이용 리팩토링
n = int(input())
my_moves = list(input().split())

move_list = ['L', 'R', 'U', 'D']
move_x = [0, 0, -1, 1]
move_y = [-1, 1, 0, 0]
x, y = 1, 1

for move in my_moves:
  for i in range(len(move_list)):
    if move == move_list[i]:
      nx = x + move_x[i]
      ny = y + move_y[i]
  
  if nx < 1 or nx > n or ny < 1 or ny > n:
    continue
  
  x, y = nx, ny
    
print(x, y)

# 맵 밖으로 나가면 다시 안으로 집어넣기