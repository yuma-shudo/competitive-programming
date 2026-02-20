#!/bin/bash
# 使い方: ./run.sh AtCoder/2025-02-20/abc390_a

DIR=$1
cd "$DIR"

PASS=0
FAIL=0
SKIP=0

for in_file in in*.txt; do
  num="${in_file//[^0-9]/}"
  out_file="out${num}.txt"

  # out*.txtが空ならスキップ
  if [ ! -s "$out_file" ]; then
    echo "⏭️  Test $num: スキップ（out${num}.txtが空）"
    ((SKIP++))
    continue
  fi

  actual=$(python3 main.py < "$in_file" | tr -d '\r')
  expected=$(cat "$out_file" | tr -d '\r')

  if [ "$actual" = "$expected" ]; then
    echo "✅ Test $num: AC"
    ((PASS++))
  else
    echo "❌ Test $num: WA"
    echo "  Expected: $expected"
    echo "  Actual:   $actual"
    ((FAIL++))
  fi
done

echo ""
echo "Result: ${PASS} AC / $((PASS+FAIL)) tests  (${SKIP} skipped)"