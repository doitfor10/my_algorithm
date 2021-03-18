#프로그래머스 두 개 뽑아서 더하기 https://programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    for n in range(len(numbers)-1):
        for m in range(1+n,len(numbers)):
            answer.append(numbers[n]+numbers[m])
            #중복제거 후 리스트화해서 sorted
    return sorted(list(set(answer)))

print(solution([2,1,3,4,1]))