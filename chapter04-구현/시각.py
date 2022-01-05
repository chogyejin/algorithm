# 113p 예제 4-2 시각
# N 입력 받고 N시 59분 59초 중에 3 들어간 시각 개수

n = int(input())

count = 0
for i in range(n+1):
  for j in range(60):
    for k in range(60):
      if '3' in (str(i) + str(j) + str(k)):
        count += 1

print(count)

# range(n)이면 n이 포함 안 되기 때문에 n+1로 n까지 포함시킴