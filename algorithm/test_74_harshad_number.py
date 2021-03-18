#프로그래머스 하샤드 수 https://programmers.co.kr/learn/courses/30/lessons/12947
def solution(x):
    
    if x<=10:
        return True
    num_word = str(x)
    sum_num = 0
    for n in num_word:
        sum_num+=int(n)
    
    if x % sum_num == 0:
        return True
    else:
        return False
    
x = int(input())
print(solutuin(x))