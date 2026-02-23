import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(i, -1, -1):
            if i == j:
                dp[j][i] = a[i]
                continue
            pick_left = a[j] - dp[i][j+1]
            pick_right = a[i] - dp[i-1][j]
            dp[i][j] = max(pick_left, pick_right)
    # print(dp)
    print(dp[n-1][0])

main()