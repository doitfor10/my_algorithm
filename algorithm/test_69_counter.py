#백준 통계학 https://www.acmicpc.net/problem/2108
#타임초과가 떠서 counter를 통해 다시 구함.
import sys
from collections import Counter

case = int(sys.stdin.readline())
number = []
for _ in range(case):
  number.append(int(sys.stdin.readline()))

print(round(sum(number)/case))
print(sorted(number)[(len(number)//2)])

#리스트에 담긴 튜플형태로 반환됨.
mode = Counter(sorted(number)).most_common()
if len(number)>1 and mode[0][1] == mode[1][1]:
  print(mode[1][0])
else:
  print(mode[0][0])

print(max(number)-min(number))


#타임 초과.. 이전 코드
import sys
case = int(sys.stdin.readline())
number = []
for _ in range(case):
  number.append(int(sys.stdin.readline()))

compare = []
for n in range(len(number)):
  compare.append(number.count(number[n]))

print(round(sum(number)/case))
print(sorted(number)[(len(number)//2)])
if compare.count(max(compare))>1:
  mode = set()
  for i in range(len(compare)):
    if max(compare) == compare[i]:
      mode.add(number[i])
  mode = sorted(mode)
  print(mode[1])
else:
  print(number[compare.index(max(compare))])
print(max(number)-min(number))