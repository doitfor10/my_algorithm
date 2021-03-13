
# p,y의 개수가 같은지 아닌지를 판별하는 문제.
def solution(s):
    return True if s.lower().count('p') == s.lower().count('y') else False