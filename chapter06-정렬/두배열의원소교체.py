# 182p 예제 6-4 두 배열의 원소 교체
# N개 원소, K번 바꿔치기, 배열 A B
# 배열 A의 합이 최대가 되도록 교환, 합 출력

n, k = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

sum_array = []
for i in range(k):
  a[i], b[i] = b[i], a[i]
  result = sum(a)
  sum_array.append(result)

print(max(sum_array))

# 원소가 작은 경우에만 swap 하고 배열 합 출력
for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break

print(sum(a))

# 나는 k번 동안 모두 swap을 하고 배열의 합을 저장하는 리스트의 max를 출력
# 두 번째 방법은 배열 A의 원소가 B의 원소보다 작을 때만 swap하여 합 최대화 후 sum(a) 출력