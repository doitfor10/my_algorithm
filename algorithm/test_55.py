# 백준 2609번 https://www.acmicpc.net/problem/2609
# 두 수의 최대공약수와 최소공배수 구하기.

a,b = map(int,input().split())

def divisor(n,m):
 
  if n<m:
    n,m=m,n
  mod = n%m
  while mod > 0:
     n = m 
     m = mod
     mod = n%m
  return m

print(divisor(a,b))
print(int(a*b/divisor(a,b)))


 