# 백준 11399번 https://www.acmicpc.net/problem/11399
# 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값 구하기.

import sys
case = int(sys.stdin.readline())
people_time = list(map(int,sys.stdin.readline().split()))
people_time.sort() #가장 빨리 걸리는 사람부터 처리하면 된다. 
time = 0
min_time =[]

for t in people_time:
  time += t
  min_time.append(time)

print(sum(min_time))
