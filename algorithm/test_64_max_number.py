#백준 최댓값과 위치 찾기 https://www.acmicpc.net/problem/2562

num = []
for _ in range(9):
  num.append(int(input()))

print(max(num))
print(num.index(max(num))+1)