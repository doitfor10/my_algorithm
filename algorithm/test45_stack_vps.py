#스택 vps 여부 검사
case = int(input())

for _ in range(case):
  bracket = list(input())
  stack = []
  no_vps = 0
  if len(bracket)%2 !=0: # 홀수면 애초에 짝이 안맞음!
    print('NO')
  
  elif bracket[0] ==')' or bracket[-1] =='('  : #시작과 끝이 짝이 안맞을 때
    print('NO')

  else:
   for b in bracket:
     if b =='(':
       stack.append(b)
     if b==')':
      if len(stack)==0:
        no_vps = 1 #no 여부 체크 
        break
      else:
        stack.pop()

   if len(stack) == 0 and no_vps == 0:
      print('YES')
   else:
      print('NO')
