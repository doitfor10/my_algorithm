# 백준 1037번 약수 https://www.acmicpc.net/problem/1037
# 1과 본인을 제외한 N의 약수가 주어졌을 때 N 구하기
count = int(input())
number_list = list(map(int,input().split()))
print(min(number_list)*max(number_list))