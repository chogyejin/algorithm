# 118p 예제 4-3 게임 개발
# 현재 방향에서 반시계로 돎
# 안 간 곳 있으면 이동, 간 칸이면 또 돎
# 4방향 모두 갔거나 바다면 뒤로 한 칸, 뒤쪽이 바다면 멈춤
# 이동한 칸의 개수

n, m = map(int,input().split())
x, y, direction = map(int,input().split())

# 입력 맵 데이터
input_map = []
for i in range(n):
  input_map.append(list(map(int,input().split())))

# 방문한 곳 기록한 맵 데이터
visited_map = [[0] * m for _ in range(n)]

move_x = [-1, 0, 1, 0] # 북 동 남 서
move_y = [0, 1, 0, -1]

count = 1
turn = 0
visited_map[x][y] = 1 # 현재좌표는 방문
while True:
  # 반시계 회전
  direction -= 1
  if direction == -1: # 북 -> 서
    direction = 3

  temp_x = x + move_x[direction]
  temp_y = y + move_y[direction]

  # 방문한 적 없고 바다가 아니면
  # 이동하고 방문찍고 count++, turn 초기화
  if visited_map[temp_x][temp_y] == 0 and input_map[temp_x][temp_y] == 0:
    x = temp_x
    y = temp_y
    visited_map[temp_x][temp_y] = 1
    count += 1
    turn = 0
    continue

  # 방문 못하면 turn++
  else:
    turn += 1

  # 4방향 다 돌면
  if turn == 4:
    temp_x = x - move_x[direction]
    temp_y = y - move_y[direction]

    # 방문은 했었지만 갈 수 있는 곳으로 감
    if input_map[temp_x][temp_y] == 0:
      x = temp_x
      y = temp_y 
      turn = 0
    else:
      break

print(count)

# 리스트 컴프리헨션으로 초기화
# 현재 좌표 방문 처리 미리
# 방향 이동 시엔 x, y 이동 리스트 만들자
# 시나리오 완성하면 순서대로 옮기자 