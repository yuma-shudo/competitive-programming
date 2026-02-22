import sys
input = sys.stdin.readline

def main():
    n, W = map(int, input().split())
    # dp = [-1]*(W+1)
    # dp[0] = 0
    dp = [0] * (W + 1)

    for _ in range(n):
        w, v = map(int, input().split())
        # next_dp = dp.copy()
        # for i in range(W+1):
        #     if dp[i] != -1 and i+w <= W:
        #         next_dp[i+w] = max(dp[i+w], dp[i] + v)
        # dp = next_dp.copy()
        for i in range(W, w - 1, -1):
            if dp[i - w] + v > dp[i]:
                dp[i] = dp[i-w] + v
    
    print(max(dp))

main()