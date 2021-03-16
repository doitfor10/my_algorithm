#백준 나머지 https://www.acmicpc.net/problem/3052

num_list =[]
for _ in range(10):
  num = int(input())
  num_list.append(num%42)

print(len(set(num_list)))