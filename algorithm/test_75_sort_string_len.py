#프로그래머스 문자열 내 마음대로 정렬하기 https://programmers.co.kr/learn/courses/30/lessons/12915
#들어오는 배열에서 n번째 index를 기준으로 배열하기. 
def solution(strings, n):
    return sorted(strings,key=lambda x: (x[n],x))

strings = ["sun", "bed", "car"]
print(solution(strings,1))