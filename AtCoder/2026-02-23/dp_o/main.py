import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    mod = 10**9 + 7
    dp = [0] * (1<<n)
    dp[0] = 1
    for i in range((1<<n) - 1):
        man = i.bit_count()
        if man == n:
            continue
        for j in range(n):
            if a[man][j] == 1 and not (i >> j) & 1:
                dp[i | (1 << j)] += dp[i]
                dp[i | (1 << j)] %= mod
    print(dp[(1<<n)-1])

main()