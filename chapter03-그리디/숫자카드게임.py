# 96 예제 3-3 큰 수의 법칙
# N X M, 각 행 중 가장 낮은 숫자를 뽑고 그 중 가장 큰 숫자 출력

n, m = map(int,input().split())

result = 0
for i in range(n):
  data = list(map(int,input().split()))
  min_value = min(data)
  result = max(result, min_value)

print(result)

# N행 동안 반복하고 각 행마다 min 값 찾음
# result(초기 0)와 min 값 중 큰 값 result로 선택 반복