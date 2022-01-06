# 115p 예제 4-2 왕실의 나이트
# 좌표(가로-a~h, 세로-1~8) 입력받아 나이트의 이동가능한 경우의 수 출력 

coord = input() #string

# ord('a') = 97
col = ord(coord[0]) - 96
row = int(coord[1])

move_col = [-1, 1, -2, 2, -2, 2, -1, 1]
move_row = [-2, -2, -1, -1, 1, 1, 2, 2]

count = 0
for i in range(8):
  temp_col = col + move_col[i]
  temp_row = row + move_row[i]
  
  # 이동 안되면
  if temp_col < 1 or temp_row < 1 or temp_col > 8 or temp_row > 8:
    continue

  count += 1

print(count)

# input()으로 받은 문자열은 보기에 숫자여도 모두 문자
# ord(문자)로 문자를 숫자로 변환