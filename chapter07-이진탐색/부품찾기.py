# 197p 예제 7-2 부품 찾기
# 가게 n개 부품, 개행, 부품 번호 입력
# 손님 m개 찾기, 개행, 부품 번호 입력
# 있는지 없는지 no yes로 출력

n = int(input())
data_list = list(map(int,input().split()))
m = int(input())
find_list = list(map(int,input().split()))

# data_list 정렬하고 find_list 하나씩 찾기
data_list.sort()

def binary_search(array, target, start, end):
  if start > end:
    return None
  
  mid = (start + end) // 2

  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search(array, target, start, mid - 1)
  else:
    return binary_search(array, target, mid + 1, end)

for i in find_list:
  result = binary_search(data_list, i, 0, n - 1)

  if result == None:
    print('no', end=' ')
  else:
    print('yes', end=' ')

# 이진 탐색 이용, 찾으려는 source 리스트 정렬 후 인자로 넘겨주기
