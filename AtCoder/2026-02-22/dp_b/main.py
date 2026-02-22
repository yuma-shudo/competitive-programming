import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    dp = [0]*n

    for i in range(1, n):
        if i < k:
            dp[i] = abs(h[i] - h[0])
            continue
        cost = float("inf")
        for back in range(1, k+1):
            cost = min(cost, dp[i-back] + abs(h[i] - h[i-back]))
        dp[i] = cost
    print(dp[n-1])

main()