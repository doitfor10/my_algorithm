#백준 평균 https://www.acmicpc.net/problem/1546

case =int(input())
avg = list(map(int,input().split()))
new_avg = 0
max_num = max(avg)
for i in avg:
  new_score = i/max_num*100
  new_avg+= new_score

print(new_avg/case)