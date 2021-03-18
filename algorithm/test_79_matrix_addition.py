#프로그래머스 행렬의 덧셈 https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer2 = []
        for j in range(len(arr1[i])):
            answer2.append(arr1[i][j]+arr2[i][j])
        answer.append(answer2)
    return answer

print(solution([[1,2],[2,3]],[[3,4],[5,6]]))