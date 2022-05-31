function solution(routes) {
  let answer = 0;
  routes.sort((a, b) => a[1] - b[1]); // 나가는 지점 오름차순 정렬

  while (routes.length !== 0) {
    const point = routes.shift()[1]; // 맨앞 shift

    for (let i = 0; i < routes.length; i++) {
      if (point >= routes[i][0]) {
        routes.splice(i, 1); // 해당 route 제거
        i--; // 제거하고 다시 맨앞 선택해야 되기 때문에 i--
      }
    }

    answer++;
  }
  return answer;
}
