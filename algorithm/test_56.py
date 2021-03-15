# 백준 1934 최소공배수 구하기 https://www.acmicpc.net/problem/1934


case = int(input())

def divisor(n,m):
 
  if n<m:
    n,m=m,n
  mod = n%m
  while mod > 0:
     n = m 
     m = mod
     mod = n%m
  return m

for _ in range(case):
  a,b = map(int,input().split())
  print(int(a*b/divisor(a,b)))