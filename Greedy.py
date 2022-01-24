# 백준 단계별로 풀어보기 - Greedy 문제

#11047 동전0
import sys
# N, K = map(int, sys.stdin.readline().split())
N, K = map(int, input().split())

coins = []
for n in range(N):
    coins.append(int(sys.stdin.readline()))

# 여기서부터 그리디 알고리즘 시작
numbers = 0
for _ in range(N-1,-1,-1):
    numbers += K // coins[_]
    K %= coins[_]
    if K == 0:
        break

print(numbers)