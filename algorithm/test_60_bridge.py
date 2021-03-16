# 백준 https://www.acmicpc.net/problem/1010
# 주어진 서,동쪽 사이트에 따라 다리를 지을 수 있는 경우의 수 구하기.
# 순서없는 조합 가짓수. 콤비네이션 nCm
import sys
case = int(sys.stdin.readline())

def factorial(number):
    return number * factorial(number-1) if number>1 else 1

for _ in range(case):
  N,M = map(int,sys.stdin.readline().split())
  # N이 1인 경우는 경우의 수가 M만큼.
  # N이 M과 같은 경우는 경우의 수가 1
  if N == 1:
    print(M)
  elif N ==M:
    print(1)
  else:
    print(int(factorial(M)/(factorial(N)*factorial(M-N))))

  
