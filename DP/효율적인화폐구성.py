# 226p 예제 8-5 효율적인 화폐 구성
# N개, M원 만들기, 1 <= N <= 100, 1 <= M <= 10000
# 불가능할 때 -1 

n, m = map(int,input().split())
coin_list = []
for i in range(n):
  coin_list.append(int(input()))

table = [99999] * 10001 # 테이블에 화폐 개수 저장
table[0] = 0

for i in range(len(coin_list)): # 코인 개수만큼 반복
  for j in range(coin_list[i], m + 1): # 코인 첫 단위 값을 인덱스의 시작으로 m까지
    table[j] = min(table[j], table[j - coin_list[i]] + 1)

for i in range(1,m+1):
  print(i, table[i])

if table[m] >= 99999:
  print(-1)  
else:
  print(table[m])

# table 값이 99999인 것은 만들 수 없다는 뜻, 만들 수 있으면 table 갱신
# 코인 단위 별로 table[코인 처음 값] ~ table[마지막] 갱신