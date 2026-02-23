# # dp[j] = 重さjのとき最大価値
# dp = [0] * (W + 1)

# for w, v in items:
#     for j in range(W, w - 1, -1):  # 逆順（二重使用防止）
#         dp[j] = max(dp[j], dp[j - w] + v)

# print(max(dp))

# # dp[j] = 価値jを達成する最小重さ
# max_v = n * max_value
# dp = [float('inf')] * (max_v + 1)
# dp[0] = 0

# for w, v in items:
#     for j in range(max_v, v - 1, -1):  # 逆順（同じ理由）
#         dp[j] = min(dp[j], dp[j - v] + w)

# ans = next(j for j in range(max_v, -1, -1) if dp[j] <= W)
# print(ans)

# n = len(a)
# dp = [[0] * n for _ in range(n)]



# 区間長1の初期値
# for i in range(n):
#     dp[i][i] = ...

# # 区間長を2, 3, ...と伸ばしていく（重要！）
# for length in range(2, n + 1):
#     for l in range(n - length + 1):
#         r = l + length - 1
#         # 区間[l, r]をどこかで分割して最適値を求める
#         for mid in range(l, r):
#             dp[l][r] = max(dp[l][r],
#                           dp[l][mid] + dp[mid+1][r] + ...)

import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    mod = 10**9 + 7

    dp = [0] * (1 << n)
    dp[0] = 1  # 誰も割り当てていない状態が1通り

    for i in range(1 << n):
        man = i.bit_count()  # i番目の状態で何人目の男性を割り当てるか
        if man == n:
            continue
        for j in range(n):   # j番目の女性に割り当てを試みる
            if a[man][j] == 1 and not (i >> j) & 1:  # 相性良い & 未割り当て
                dp[i | (1 << j)] = (dp[i | (1 << j)] + dp[i]) % mod

    print(dp[(1 << n) - 1])

main()

# ビット演算チートシート
# i.bit_count()  → 立っているビット数（割り当て済み人数）
# (i >> j) & 1   → j番目のビットが立っているか
# i | (1 << j)   → j番目のビットを立てる