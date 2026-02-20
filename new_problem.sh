#!/bin/bash
# 使い方: ./new_problem.sh https://atcoder.jp/contests/abc390/tasks/abc390_a

URL=$1

# tasks/ 以降をタスク名として取得（コンテスト名に依存しない）
TASK=$(echo "$URL" | grep -oP '(?<=tasks/)[^/]+$')

if [ -z "$TASK" ]; then
  echo "❌ URLの形式が正しくありません"
  echo "例: ./new_problem.sh https://atcoder.jp/contests/abc390/tasks/abc390_a"
  exit 1
fi

DATE=$(date +%Y-%m-%d)
DIR="AtCoder/$DATE/${TASK}"

mkdir -p "$DIR"
cp template.py "$DIR/main.py"

for i in 1 2 3; do
  touch "$DIR/in${i}.txt" "$DIR/out${i}.txt"
done

echo "✅ Created: $DIR"
echo "🔗 Problem: $URL"

code "$DIR/main.py"