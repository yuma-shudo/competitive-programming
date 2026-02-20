import bisect
import math
import sys
sys.setrecursionlimit(10**6)
import copy
#import numpy as np # Pypyでは使えない
import heapq
from collections import deque,defaultdict,Counter
from itertools import permutations,combinations,product,accumulate
from array import array # 連続メモリ上の配列（数値型で使用，高速）
# al=[chr(ord('a') + i) for i in range(26)]
# Al=[chr(ord('A') + i) for i in range(26)]
input = sys.stdin.read
data = input().split()
iterator = iter(data)
# n = int(next(iterator))
# s = next(iterator)
# a = [int(next(iterator)) for _ in range(n)]

def bfs(start_y, start_x, H, W, grid):
    """幅優先探索で到達可能なマスを探索"""
    visited = [[False] * W for _ in range(H)]
    q = deque()
    q.append((start_y, start_x))
    visited[start_y][start_x] = True

    # 上下左右の移動方向
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        y, x = q.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            
            # 範囲内かチェック
            if 0 <= ny < H and 0 <= nx < W:
                # 未訪問かつ壁でないなら進む
                if not visited[ny][nx] and grid[ny][nx] != "#":
                    visited[ny][nx] = True
                    q.append((ny, nx))
    return visited
def solve():
    # 1. 入力をすべて読み込み、空白/改行区切りでリスト化
    data = input().split()
    iterator = iter(data)

    try:
        # 2. イテレータから順番に取り出す
        H = int(next(iterator))
        W = int(next(iterator))
        
        # グリッドの読み込み
        # next(iterator) は1行分の文字列 ("....#") を返します
        # list() で囲むことで [' .', '.', '.', '.', '#'] のように文字配列化し、変更可能にします
        grid = [list(next(iterator)) for _ in range(H)]

    except StopIteration:
        return

    # --- メイン処理 ---
    
    # スタート地点 (0, 0) と仮定（問題に応じて変更してください）
    start_y, start_x = 0, 0

    # スタート地点が壁でないか確認（念の為）
    if grid[start_y][start_x] == "#":
        # スタート不可の場合、全てFalseの配列を用意するだけ
        visited = [[False] * W for _ in range(H)]
    else:
        visited = bfs(start_y, start_x, H, W, grid)

    # 結果表示（到達可能なら "o", 不可なら "x"）
    # 出力行数が多い場合、printを繰り返すよりリストに貯めて join する方が高速です
    result = []
    for y in range(H):
        row_str = "".join("o" if visited[y][x] else "x" for x in range(W))
        result.append(row_str)
    
    print('\n'.join(result))
if __name__ == "__main__":
    solve()

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
    
from functools import cmp_to_key
# 点 p がどの領域にあるかを判定する関数
# 上半分（y > 0 または y=0かつx>=0）を 0
# 下半分（y < 0 または y=0かつx<0）を 1
# とする（これで 0度〜360度 の順になる）
def get_quadrant(p):
    x, y = p
    if y > 0 or (y == 0 and x >= 0):
        return 0
    return 1

# 比較関数
def compare(p1, p2):
    # 1. 領域（象限）が違うなら、領域の番号で比較
    q1 = get_quadrant(p1)
    q2 = get_quadrant(p2)
    if q1 != q2:
        return q1 - q2
    
    # 2. 同じ領域なら外積（クロス積）で比較
    # p1 x p2 = x1*y2 - x2*y1
    # 外積 > 0 なら p1 は p2 より時計回り（p2の方が角度が大きい）
    # 外積 < 0 なら p1 は p2 より反時計回り（p1の方が角度が大きい）
    x1, y1 = p1
    x2, y2 = p2
    cross_product = x1 * y2 - x2 * y1
    
    # 外積が正 = 左側にある = 角度が小さい (反時計回りの場合)
    # ここではPythonのsort仕様に合わせて、
    # 負なら p1 < p2, 正なら p1 > p2 となるように返す
    # (反時計回りに並べたい -> 外積が正なら p1 が手前 -> p1 < p2 としたい)
    # よって -cross_product を評価する
    return -cross_product

# points = [
#     (1, 1), (-1, 1), (-1, -1), (1, -1), (1, 0)
# ]

# # ソート実行
# points.sort(key=cmp_to_key(compare))
# # 結果: (1, 0) -> (1, 1) -> (-1, 1) -> (-1, -1) -> (1, -1)
# # (X軸正方向から反時計回り)