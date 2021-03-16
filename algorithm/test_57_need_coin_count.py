# 백준 동전 0 https://www.acmicpc.net/problem/11047
# K원을 만드는데 필요한 동전 개수의 최솟값 구하기. 
import sys
N,K = map(int,sys.stdin.readline().split())
coin_list = []

for _ in range(N):
  coin = int(sys.stdin.readline())
  if K>=coin:   # 나눌 수 없는 동전들은 빼고 받음.
    coin_list.append(coin)

coin_count = 0

for n in range(1,len(coin_list)+1):
  divide = coin_list[-n] #큰 동전부터 비교.
  divide_coin = K//divide #4
  coin_count+= divide_coin
  K -= divide_coin* divide
  
print(coin_count)

