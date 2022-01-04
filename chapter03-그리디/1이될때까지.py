# 99 예제 3-4 1이 될 때까지
# N이 1이 될 때까지 -1 하거나 K로 나눔
# 2 <= N <= 100,000, 2 <= K <= 100,000

# 간단한 풀이 (1을 계속해서 빼줌)
n, k = map(int,input().split())

count = 0
while True:
  if n % k == 0:
    n //= k
  elif n % k != 0:
    n -= 1
  
  count += 1
  if n == 1:
    break;
  
print(count)

# 효율적 풀이 (뺄 1을 뭉쳐서 한 번에 빼기)
n, k = map(int,input().split())

count = 0
while True:
  target = (n // k) * k
  count += n - target
  n = target

  # N이 K보다 작아지면 break
  if n < k:
    break;
  
  count += 1
  n //= k

count -= 1 # n이 0이 될 때까지 뺀 거라 1만큼 덜 더해줌
print(count)

# 나누기가 더 빠르게 숫자를 감소시킴