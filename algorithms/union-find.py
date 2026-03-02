class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        # 各グループのサイズを管理する配列を追加（初期値は全員1人）
        self.size = [1] * (n + 1)

    def find(self, x):
        if self.parent[x] == x:
            return x
        # 経路圧縮
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
            
        # サイズによる併合 (Union by size)
        # 常に py の方がサイズが大きくなるようにスワップ
        if self.size[px] > self.size[py]:
            px, py = py, px
            
        self.parent[px] = py
        self.size[py] += self.size[px] # サイズを更新
        return True

    def same(self, x, y):  # 同じグループか判定
        return self.find(x) == self.find(y)