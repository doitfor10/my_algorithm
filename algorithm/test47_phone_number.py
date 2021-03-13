# 폰넘버 주어진 앞자리 가리기 

def solution(phone_number):
    first = phone_number[0:-4]
    for i in first:
        first= first.replace(i,'*')
    return  first+phone_number[-4:]