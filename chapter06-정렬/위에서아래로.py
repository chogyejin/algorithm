# 178p 예제 6-2 위에서 아래로
# N 입력, 2번째 줄부터 N+1줄까지 원소 입력, 띄어쓰기로 출력

n = int(input())

array = []
for i in range(n):
  array.append(int(input()))

array.sort(reverse=True)

for i in range(len(array)):
  print(array[i], end=' ')

# 띄어쓰기로 입력받을 땐 array = list(map(int,input().split()))
# 마지막 출력 루프에서
# for i in array:
#   print(i, end=' ') 
