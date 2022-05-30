function findParent(parent, x) {
  if (parent[x] !== x) {
    parent[x] = findParent(parent, parent[x]); // 재귀적으로 부모 찾음
  }
  return parent[x];
}

function unionParent(parent, a, b) {
  const p1 = findParent(parent, a);
  const p2 = findParent(parent, b);
  if (p1 < p2) {
    parent[p2] = p1; // 번호 작은 쪽이 부모가 되게
  } else {
    parent[p1] = p2;
  }
}

function solution(n, costs) {
  const v = n; // 정점 수
  const e = costs.length; // 간선 수
  const parent = Array.from({ length: v }, (_, i) => i); // 부모 테이블 자신으로 초기화
  costs.sort((a, b) => a[2] - b[2]); // 비용 오름차순 정렬

  let result = 0;
  costs.forEach(([a, b, cost], i) => {
    // console.log(i, parent)
    // 사이클 발생 안 하면 부모 union (사이클 발생하면 신장트리에 포함 X)
    if (findParent(parent, a) !== findParent(parent, b)) {
      unionParent(parent, a, b);
      result += cost;
    }
  });
  return result;
}
