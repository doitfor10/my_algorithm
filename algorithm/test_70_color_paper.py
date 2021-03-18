#백준 색종이 만들기 https://www.acmicpc.net/problem/2630
import sys
length = int(sys.stdin.readline())
white_count = 0 #0
blue_count = 0 #1
paper = []

for _ in range(length):
  paper.append(list(map(int,sys.stdin.readline().split())))


# [1 1 0 0 0 0 1 1]
# [1 1 0 0 0 0 1 1]
# [0 0 0 0 1 1 0 0]
# [0 0 0 0 1 1 0 0]
# [1 0 0 0 1 1 1 1]
# [0 1 0 0 1 1 1 1]
# [0 0 1 1 1 1 1 1]
# [0 0 1 1 1 1 1 1]

def cut(x,y,n):
  global white_count,blue_count
  check = paper[x][y]
  for i in range(x,x+n):
    for j in range(y,y+n):
      if check != paper[i][j]:
        #4등분..
        cut(x,y,n//2)
        cut(x,y+n//2,n//2)
        cut(x+n//2,y,n//2)
        cut(x+n//2,y+n//2,n//2)
        return 
  if check:
    blue_count+=1
    return
  else:
    white_count+=1
    return

cut(0,0,length)
print(white_count)
print(blue_count)

    
    