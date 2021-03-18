#백준 다이얼 https://www.acmicpc.net/problem/5622

number = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

N = input()
count = 0
for i in range(len(N)):
  for n in number:
    if N[i] in n:
      count+= number.index(n)+3
print(count)