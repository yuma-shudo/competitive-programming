from collections import deque

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
