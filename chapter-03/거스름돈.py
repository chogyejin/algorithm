# 87p 예제 3-1 거스름돈
# 손님에게 거슬러 줘야 할 돈 N원, 동전의 최소 개수

n = int(input('얼마인지 입력: '))
count = 0
coin_types = [500,100,50,10]

for coin in coin_types:
  count += n // coin
  n %= coin

print(count)

# 큰 단위부터 차례대로? 큰 단위가 모두 작은 단위의 배수임
# 그리디가 안되면 DP나 graph 고려