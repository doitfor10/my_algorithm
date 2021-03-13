# queue 함수 구현
import sys
from collections import deque

case = int(sys.stdin.readline())
queue = deque()

for _ in range(case):
  command = sys.stdin.readline().split()
  
  if command[0] =='push':
    queue.append(int(command[1]))
  elif command[0]=='pop':
    if len(queue) ==0:
      print(-1)
    else:
      print(queue.popleft())
  elif command[0]=='size':
    print(len(queue))
  elif command[0]=='empty':
    if len(queue) == 0:
      print(1)
    else:
      print(0)
  elif command[0]=='front':
    if len(queue) ==0:
      print(-1)
    else:
      print(queue[0])
  elif command[0]=='back':
    if len(queue) ==0:
      print(-1)
    else:
      print(queue[-1])