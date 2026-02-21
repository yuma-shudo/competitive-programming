# 「x以上の最小インデックス」を返す（bisect_leftと同等）
def binary_search(a, x):
    lo, hi = 0, len(a)      # 答えの候補範囲は [lo, hi)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1    # midは確実にNG → 右を探す
        else:
            hi = mid        # midがOKかも → hiを縮める
    return lo