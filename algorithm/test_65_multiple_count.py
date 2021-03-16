#백준 숫자의 개수https://www.acmicpc.net/problem/2577

num = []
for _ in range(3):
  num.append(int(input()))

multiple = str(num[0]*num[1]*num[-1])

for c in range(10):
  print(multiple.count(str(c)))