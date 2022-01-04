# 92p 예제 3-2 큰 수의 법칙
# N개 숫자, M번 더하기, 연속 K번 사용

n, m, k = map(int,input().split())
naturalNumbers = list(map(int,input().split()))

naturalNumbers.sort(reverse=True)
first = naturalNumbers[0]
second = naturalNumbers[1]

result = 0
nums = first * k + second * 1
quotient = m // (k + 1)
remainder = m % (k + 1)

if remainder == 0: # M이 k+1 배수면
  result = nums * quotient
elif remainder != 0: # M이 k+1 배수 아니면
  result = (nums * quotient) + (first * remainder)

print(result)

# 반복되는 수열에 초점
# 예시를 나열해보고 규칙 찾자