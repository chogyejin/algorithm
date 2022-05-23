// 제일 무거운 놈이랑 가벼운 놈 태워서 보내자
function solution(people, limit) {
  let count = 0;
  people.sort((a, b) => b - a);
  for (let i = 0; i < people.length; i++) {
    if (people[i] + people[people.length - 1] <= limit) {
      people.pop();
    }
    count++;
  }

  return count;
}
