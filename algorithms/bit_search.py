import sys
# 入力を高速化するための定型文です
input = sys.stdin.readline

def main():
    # 1. 入力の受け取り（問題に合わせて変更してください）
    # n: 要素の数（例: n個の品物、n個のスイッチなど）
    n, m = map(int, input().split())
    
    # 2. 答えを保持する変数の初期化
    # 最小値を求めたい場合は float('inf')、最大値の場合は 0 や -float('inf') などを設定します
    ans = float('inf')

    # 3. bit全探索のループ (0 から 2^n - 1 まで)
    # 1 << n は 2のn乗 を意味します。これで全ての組み合わせ（選ぶ/選ばない）を網羅します
    for i in range(1 << n):
        
        # この組み合わせ(i)における、一時的な合計値や状態を保持する変数を準備します
        current_val = 0
        is_valid = True # 条件を満たすかどうかのフラグ
        
        # n個の要素それぞれについて、選ぶか選ばないかを確認します
        for j in range(n):
            
            # i を右に j ビットずらして 1 との論理積をとります
            # これにより「i の j 番目のビットが 1 かどうか（選ぶかどうか）」を判定できます
            if (i >> j) & 1:
                # --- j番目の要素を「選ぶ」場合の処理 ---
                # 例: current_val += cost[j]
                pass
            else:
                # --- j番目の要素を「選ばない」場合の処理（必要な場合のみ） ---
                pass
                
        # 4. 1つの組み合わせ(i)の処理が終わったら、条件判定と答えの更新を行います
        # 例: もし条件を満たしていれば、ans を更新する
        # if is_valid:
        #     ans = min(ans, current_val)

    # 5. 最終的な答えを出力します
    # 条件を満たすものがなかった場合の処理（ans が初期値のままかどうか）も考慮すると安全です
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()