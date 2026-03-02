class FenwickTree:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        """i番目までの累積和 (1-indexed)"""
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        """i番目にxを加算 (1-indexed)"""
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def lower_bound(self, w):
        """
        累積和が w 以上になる最小のインデックスを返す
        （＝小さい方から w 番目の要素が、座標圧縮後の何番目にあるか）
        """
        if w <= 0: return 0
        x = 0
        r = 1
        while r < self.size:
            r <<= 1
        
        while r > 0:
            if x + r <= self.size and self.tree[x + r] < w:
                w -= self.tree[x + r]
                x += r
            r >>= 1
        return x + 1