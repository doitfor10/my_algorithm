#10773번 제로 

import sys

case = int(sys.stdin.readline())
stack = []
for _ in range(case):
  number = int(sys.stdin.readline())
  if number == 0:
    if len(stack)!=0: #적은 수가 있다면..
      stack.pop()
  
  else:
    stack.append(number) #올바른 수.

print(sum(stack)) #남은 올바른 수의 합 