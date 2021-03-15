# 백준 9184 신나는 함수 실행
# 딕셔너리의 키로 튜플을 사용 
import sys

#딕셔너리에 기록해서 사용
record ={

}

def w(a,b,c):

  if (a,b,c) in record:
    return record[(a,b,c)]

  if a<= 0 or b<=0 or c<=0:
    return 1
  
  elif a>20 or b>20 or c>20:
    return w(20,20,20) #범위 조정 
  
  elif a<b and b<c:

    num = w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
    record[(a,b,c)] = num
    return num

  else:
    num = w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
    record[(a,b,c)] = num
    return num 


while True:
  a,b,c = map(int,sys.stdin.readline().split())
  if a == -1 and b ==-1 and c ==-1:
    break
  print(f'w({a}, {b}, {c}) = {w(a,b,c)}')