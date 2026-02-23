class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # 最初は自分が根

    def find(self, x):  # 根を探す（経路圧縮）
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):  # グループを合併
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[px] = py

    def same(self, x, y):  # 同じグループか判定
        return self.find(x) == self.find(y)