# 프로그래머스 > 정렬 > level 1
# 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands
# array의 i번째부터 j번째까지 자르고
# 1에서 나온 배열을 정렬
# 2에서 나온 배열의 k 번째 수
# 나온 결과를 배열에 담아 return

def solution(array, commands):
    answer = []
    
    for command in commands:
        temp = []
        i = command[0]
        j = command[1]
        k = command[2]

        temp = array[i - 1: j]
        temp.sort()
        answer.append(temp[k - 1])
         
    return answer