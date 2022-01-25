# 220p 예제 8-3 개미전사
# 식량 창고 개수 N, 창고 당 식량 수(K) 리스트 입력받아 최대 약탈 식량 수 출력
# 3 <= N <= 100, 0 <= K <= 1000

n = int(input())
input_data = list(map(int,input().split()))
result = [0] * 100 # 테이블

result[0] = input_data[0]
result[1] = max(input_data[0], input_data[1])

for i in range(2, n): #result[n]부터 result[n - 1]까지(3번째 부터)
  result[i] = max(result[i - 1], result[i - 2] + input_data[i])

print(result[n - 1])

# i번째 식량 창고까지의 최적의 해(식량 최대 수)를 테이블에 저장(i 0부터 시작)
# i번째 기준으로 
# i-1털면 i-1까지의 최적의 해
# i-2털면 i-2번째 최적의 해 + i번째 턴 값
# 위 두 개 중 최대 값 선택해서 저장
