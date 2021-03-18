#프로그래머스 시저 암호 https://programmers.co.kr/learn/courses/30/lessons/12926
#n자리 수만큼 알파벳을 이동하여 출력하는 암호.
def solution(s, n):
    result = ''
    for char in s:
        if char ==' ':
            result+=char
        
        elif ord(char)>= 97: #소문자
            if ord(char)+n >122: #z를 넘어 a로 넘어가야할 경우..
                m = (ord(char)+n)-ord('z')
                result+= chr(ord('a')+(m-1))
            else:
                result+= chr(ord(char)+n)
        else: #대문자
            if ord(char)+n>90: #Z를 넘어 A로 넘어가야할 경우..
                m = (ord(char)+n)-ord('Z')
                result+= chr(ord('A')+(m-1))
            else:
                result+=chr(ord(char)+n)
    return result
    word ="a B z"
    print(solution(word,4))