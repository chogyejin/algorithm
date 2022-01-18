# 201p 예제 7-3 떡볶이 떡 만들기
# N개 떡, M만큼 가져갈 것, 개행, 떡 길이 입력
# 절단기 높이 최대값 출력

n, m = map(int, input().split())
data_list = list(map(int, input().split()))

def find_height(data_list, target, start, end):
  while start <= end:
    sum = 0 # 잘린 떡 길이 합
    mid = (start + end) // 2 # 중간점, 절단기 높이

    for i in data_list:
      if i - mid > 0:
        sum += i - mid
    
    if sum >= target: # 떡 잘린 게 많을 때
      start = mid + 1
    else:
      end = mid - 1

  return end

print(find_height(data_list, m, 0, max(data_list)))

# 이진 탐색 반복문 이용, 파라메트릭 서치
# 케이스 몇 개를 직접 해보면서 return 값 정하자
