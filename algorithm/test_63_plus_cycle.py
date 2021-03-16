#백준 더하기 사이클 https://www.acmicpc.net/problem/1110


N = int(input())
temp = N
count = 0 
while True:

  sum_n = 0
  if N<10:
    sum_n = N 
  else:
    sum_n = int(str(N)[0])+int(str(N)[1])
    
  N = int(str(N)[-1]+str(sum_n)[-1])
  count+=1
  if N == temp:
    break
print(count)

  