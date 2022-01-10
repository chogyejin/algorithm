# 탐색

- 많은 양의 데이터 중에서 원하는 데이터를 찾는 일
  - 대표적으로 DFS(Depth First Search), BFS(Breadth-First Search)

# 자료구조

- 데이터를 표현, 관리, 처리하기 위한 구조

  - 스택(Stack)

    - 선입후출(First In Last Out), 후입선출(Last In First Out)
    - append(), pop() 메서드 이용

    ```
    stack = []

    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    stack.pop()
    stack.append(5)
    stack.append(6)
    stack.pop()

    print(stack) # 최하단 원소부터 출력 [1, 2, 3, 5]
    print(stack[::-1]) # 최상단부터 [5, 3, 2, 1]
    ```

  - 큐(Queue)

    - 선입선출(First In First Out)
    - append(), popleft() 메서드 이용

    ```
    # collections 모듈의 deque 자료구조 이용
    from collections import deque

    queue = deque()

    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)
    queue.popleft()
    queue.append(5)
    queue.append(6)
    queue.popleft()

    print(queue) # 먼저 들어온 순서대로 deque([3, 4, 5, 6])
    queue.reverse() # 역순
    print(queue) # deque([6, 5, 4, 3])
    queue = list(queue) # list 자료형으로
    print(queue) # [6, 5, 4, 3]
    ```

# DFS

- Depth First Search, 깊이 우선 탐색
- 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
- 그래프

  - 노드(Node 혹은 정점(Vertex))가 간선(Edge)으로 인접(Adjacent)
  - 인접 행렬 : 2차원 배열로 그래프 연결 표현

  ```
  INF = 999999999 # 연결 안 됨(거리 무한)

  graph = [
      [0, 7, 5],
      [7, 0, INF],
      [5, INF, 0]
  ]
  ```

  - 인접 리스트 : 리스트로 그래프 연결 표현( (연결노드, 거리) )

  ```
  graph = [[] for _ in range(3)]

  # 노드 0
  graph[0].append((1, 7)) # 노드 1과 거리 7
  graph[0].append((2, 5)) # 노드 2와 거리 5

  # 노드 1
  graph[1].append((0, 7))

  # 노드 2
  graph[2].append((0, 5))
  ```

  - 인접 행렬과 인접 리스트 차이
    - 메모리 : 노드 많아질 수록 행렬이 메모리 낭비
    - 속도 : 특정 두 노드가 연결되어 있는지 확인은 행렬이 빠름

- 동작 과정

  1. 탐색 시작 노드를 스택(현재 위치)에 삽입하고 방문 처리
  2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있다면 스택에 삽입하고 방문 처리, 방문하지 않은 인접 노드가 잇으면 스택에서 최상단 노트 뺌
  3. 2번을 더 이상 수행할 수 없을 때까지 반복

  ```
  def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
      if not visited[i]:
        dfs(graph, i, visited)


  # 전체 그래프
  graph =[
      [],
      [2, 3, 8], # 노드 1
      [1, 7],
      [1, 4, 5],
      [3, 5],
      [3, 4],
      [7],
      [2, 6, 8],
      [1, 7] # 노드 8
  ]

  # 방문 정보
  visited = [False] * 9

  dfs(graph, 1 visited) # 1 2 7 6 8 3 4 5
  ```

# BFS

- Breadth First Search, 너비 우선 탐색
- 그래프에서 가까운 노드부터 탐색하는 알고리즘, 큐와 관련
- 일반적으로 DFS보다 수행 시간 빠름(둘 다 O(N))
- deque 자료구조 이용
- 동작 과정

  1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
  2. 큐에서 노드를 꺼내(아래부터 꺼내는 것) 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
  3. 2번을 더 이상 수행할 수 없을 때까지 반복

  ```
  from collections import deque

  def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    # 큐가 빌 때까지
    while queue:
      v = queue.popleft()
      print(v, end=' ')

      for i in graph[v]:
        if not visited[i]:
          queue.append(i)
          visited = True

  graph =[
      [],
      [2, 3, 8], # 노드 1
      [1, 7],
      [1, 4, 5],
      [3, 5],
      [3, 4],
      [7],
      [2, 6, 8],
      [1, 7] # 노드 8
  ]

  visited = [False] * 9

  bfs(graph, 1, visited) # 1 2 3 8 7 4 5 6
  ```

  - deque 자료구조 append(), popleft()

  ```
  from collections import deque

  queue = deque()

  queue.append(1)
  # queue.append(2, 3) 안 됨
  queue.append((4, 5))
  queue.append((6, 7))

  a = queue.popleft()
  b = queue.popleft()
  c, d = queue.popleft()

  print(a, b, c, d) # 1 (4, 5) 6 7
  print(type(a), type(b), type(c), type(d)) # int tuple int int

  ```
