# 백준 1149 RGB거리 https://www.acmicpc.net/problem/1149
# 첫번째 집을 건너 다음집부터 자기 위치에 맞지 않는 지난 집의 
# 비용 최솟값을 구해 본인과 더한 후 저장.
# 끝까지 돌면 구한 값중에서 최솟값을 비교해 출력.

case = int(input()) 
price = []  
for i in range(case):
    price.append(list(map(int, input().split())))

for i in range(1, len(price)):
    price[i][0] = min(price[i - 1][1], price[i - 1][2]) + price[i][0]
    price[i][1] = min(price[i - 1][0], price[i - 1][2]) + price[i][1]
    price[i][2] = min(price[i - 1][0], price[i - 1][1]) + price[i][2]
print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))