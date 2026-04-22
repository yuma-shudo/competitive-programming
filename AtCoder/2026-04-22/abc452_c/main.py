import sys
input = sys.stdin.readline

def main():
    n = int(input())
    bones = []
    for _ in range(n):
        bones.append(list(map(int, input().split())))
    m = int(input())
    words = []
    for _ in range(m):
        words.append(input().rstrip())

    able = []
    for _ in range(n):
        able.append(set())

    for i in range(n):
        bone = bones[i]
        
        for word in words:
            if len(word) == bone[0]:
                able[i].add(word[bone[1] - 1])

    for word in words:
        if len(word) != n:
            print("No")
            continue
        
        is_ok = True
        for i in range(n):
            if word[i] not in able[i]:
                is_ok = False
                break 
        
        if is_ok:
            print("Yes")
        else:
            print("No")

main()