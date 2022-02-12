# 238pp 예제 10-2 팀 결성
# 학생 0번 ~ N번(N + 1개), M개 연산
# 합치기 연산 : 0 a b, 같은 팀 확인: 1 a b (a, b <= N)
# 같은 팀 확인 연산에 대한 결과 YES or NO 출력

n, m = map(int, input().split())
parent = [0] * (n + 1) # 부모 초기화
for i in range(0, n + 1): # 자기 자신으로 부모 초기화
  parent[i] = i

# 같은 팀 확인
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 합치기 연산
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a < b:
    parent[b] = a
  else:
    parent[a] = b

for i in range(m):
  operation, a, b = map(int, input().split())

  if  operation == 0: # 합치기 연산
    union_parent(parent, a, b)
  else: # 같은 팀 확인
    if find_parent(parent, a) == find_parent(parent, b):
      print("YES")
    else:
      print("NO")