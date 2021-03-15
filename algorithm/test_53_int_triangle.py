# 백준 정수 삼각형 https://www.acmicpc.net/problem/1932

import sys

case = int(sys.stdin.readline())
triagle = []
for _ in range(case):
  triagle.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,case): 
  
  for t in range(0,len(triagle[i])): 
  
    if t ==0 : #i-1도 인덱스 0번만 가능.
      triagle[i][t]+= triagle[i-1][0]
    
    elif t == len(triagle[i])-1: #마지막 인덱스라면 i-1도 마지막 인덱스만 가능.
      triagle[i][t]+= triagle[i-1][-1]
    else:
      triagle[i][t]+= max(triagle[i-1][t-1],triagle[i-1][t])

print(max(triagle[-1]))