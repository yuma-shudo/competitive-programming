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

#==========
#偏角ソート
#==========   
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

#============
#三分探索
#============
def solve():
    # 1. 入力の受け取り
    try:
        # 例: A, B を受け取る (問題に合わせて変更してください)
        A = int(next(iterator))
        B = int(next(iterator))
        
        pass 
    except StopIteration:
        return

    # 2. 評価関数 f(x) の定義
    # 下に凸（最小値を求めたい）関数を定義します
    def f(x):
        # ここに問題ごとの計算式を書く
        # 例: return B * x + A / ((x + 1) ** 0.5)
        return (x - A) ** 2 + B

    # 3. 三分探索 (探索範囲の設定)
    low = 0
    high = 10**18  # 解が存在しうる十分大きな値

    # 範囲が十分に狭くなるまでループ
    # 整数の場合、オフ・バイ・ワン(±1の誤差)を防ぐため、
    # 範囲が 2 以下になったらループを抜けて最後は全探索するのが安全です
    while high - low > 2:
        # m1: 区間の 1/3 地点, m2: 区間の 2/3 地点
        m1 = low + (high - low) // 3
        m2 = high - (high - low) // 3
        
        if f(m1) < f(m2):
            # m1 の方が値が小さい（谷底に近い）
            # → 谷底は「m2より左」にあるはず → 右側の範囲(m2 ~ high)を捨てる
            high = m2
        else:
            # m2 の方が値が小さい（谷底に近い）、または同じ
            # → 谷底は「m1より右」にあるはず → 左側の範囲(low ~ m1)を捨てる
            low = m1

    # 4. 残った狭い範囲 (low, low+1, high) を全探索して厳密な最小値を決定
    ans = float('inf')
    min_x = -1
    
    # int(low) から int(high) まで回す
    for x in range(int(low), int(high) + 1):
        val = f(x)
        if val < ans:
            ans = val
            min_x = x
            
    print(ans)
    # print(min_x) # 最小値をとる x が欲しい場合

if __name__ == "__main__":
    solve()