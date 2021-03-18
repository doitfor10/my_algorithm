#프로그래머스 콜라츠 추측 https://programmers.co.kr/learn/courses/30/lessons/12943
def solution(num):
    count = 0
    
    while True:
        
        if num == 1 :
            break
        
        if count == 500:
            count = -1
            break
        
        if num %2 == 0: #짝수
            num = num//2
        else:
            num = (num*3)+1
        count+=1
        
    return count

print(solution(626331))