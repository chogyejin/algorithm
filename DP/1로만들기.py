# 217p 예제 8-2 1로 만들기
# 정수 입력, 연산 4개 이용하여 1 만들기, 최소 연산 횟수 출력
# 5, 3, 2로 나누거나 1 빼기

x = int(input())
result = [0] * 30001

for i in range(2, x + 1): # i는 2부터 x
  # 1 빼기
  result[i] = result[i - 1] + 1
  # 2로 나누기
  if i % 2 == 0: 
    result[i] = min(result[i], result[i // 2] + 1)
  # 3으로 나누기
  if i % 3 == 0:
    result[i] = min(result[i], result[i // 3] + 1)
  # 5로 나누기
  if i % 5 == 0:
    result[i] = min(result[i], result[i // 5] + 1)

print(result[x])

# 각 숫자에 대해 연산 횟수를 result 리스트에 저장해놓음