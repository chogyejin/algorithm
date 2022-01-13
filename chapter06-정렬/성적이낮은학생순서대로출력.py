# 180p 예제 6-3 성적이 낮은 순서로 학생 출력하기
# 학생 수, 줄마다 학생이름과 점수 입력 받아 성적 오름차순 출력

n = int(input())

array = []
for i in range(n):
  input_data = input().split()
  # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
  array.append((input_data[0], int(input_data[1])))

# 람다 이용하여 정렬
array = sorted(array, key=lambda student: student[1])

for student in array:
  print(student[0], end=' ')

# 학생 정보 최대 100,000 => 계수 정렬 이용