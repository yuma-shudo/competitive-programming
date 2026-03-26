import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(a[0])
        return

    dp = [[-1, -1] for _ in range(n)]

    dp[0] = 0, a[0]
    dp[1] = dp[0][1] + a[1] * 2, a[1]

    for i in range(2, n):
        current_a = a[i]

        dp[i][0] = max(dp[i-1][1] + current_a * 2, dp[i-2][1] + current_a * 2)
        dp[i][1] = max(dp[i-1][0] + current_a, dp[i-2][0] + current_a)

    print(max(dp[n-1][0], dp[n-1][1]))

main()