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