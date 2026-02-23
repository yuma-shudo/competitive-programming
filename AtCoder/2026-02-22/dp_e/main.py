import sys
input = sys.stdin.readline

def main():
    n, W = map(int, input().split())
    dp = [float('inf')] * (10**5 + 1)
    dp [0] = 0

    for _ in range(n):
        w, v = map(int, input().split())
        for i in range(10**5, v - 1, -1):
            if dp[i - v] + w < dp[i]:
                dp[i] = dp[i - v] + w
        
    for i in range(10**5, -1, -1):
        if dp[i] <= W:
            print(i)
            return

main()