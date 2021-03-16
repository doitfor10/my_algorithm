# 백준 이항계수 https://www.acmicpc.net/problem/11050
import sys

N,K = map(int,sys.stdin.readline().split())


def factorial(number):
    return number * factorial(number-1) if number>1 else 1

# 이항 항수의 식 N!/K!(N-K)!
print(int(factorial(N)/(factorial(K)*factorial((N-K)))))

