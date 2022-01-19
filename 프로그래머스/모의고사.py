# answers 배열 입력받아서 1번찍기, 2번찍기, 3번찍기 패턴에 따라 제일 많이 맞춘 사람 출력
# 수포자 1 : 1 2 3 4 5 1 2 3 4 5 ...
# 수포자 2 : 2 1 2 3 2 4 2 5 2 1 ...
# 수포자 3 : 3 3 1 1 2 2 4 4 5 5 ...

answers = list(map(int,input().split()))
a = []
b = []
c = []

def solution(answers):
  a_count = 0
  b_count = 0
  c_count = 0
  answer = []
  for i in range(len(answers)):
    # list a
    a.append(i % 5 + 1)
        
    # list b
    if i % 2 == 0:
      b.append(2)
    elif i % 8 == 1 :
      b.append(1)
    elif i % 8 == 3:
      b.append(3)
    elif i % 8 == 5 :
      b.append(4)
    elif i % 8 == 7:
      b.append(5)
        
        
    # list c
    if i % 10 == 0 or i % 10 == 1:
      c.append(3)
    elif i % 10 == 2 or i % 10 == 3:
      c.append(1)
    elif i % 10 == 4 or i % 10 == 5:
      c.append(2)
    elif i % 10 == 6 or i % 10 == 7:
      c.append(4)
    elif i % 10 == 8 or i % 10 == 9:
      c.append(5)

    # compare with answers
    if answers[i] == a[i]:
      a_count += 1
    if answers[i] == b[i]:
      b_count += 1
    if answers[i] == c[i]:
      c_count += 1
    
    temp = []
    temp.append(a_count)
    temp.append(b_count)
    temp.append(c_count)

    if a_count == b_count and b_count == c_count:
      answer = [1, 2, 3]
    elif a_count == b_count and a_count > c_count:
      answer = [1, 2]
    elif b_count == c_count and b_count > a_count:
      answer = [2, 3]
    elif a_count == c_count and a_count > b_count:
      answer = [1, 3]
    else:
      temp.sort(reverse=True)
      if temp[0] == a_count:
        answer = [1]
      elif temp[0] == b_count:
        answer = [2]
      elif temp[0] == c_count:
        answer = [3]

  return answer

print(solution(answers))