import sys
input = sys.stdin.readline

def main():
    s = input().rstrip()
    if len(s) % 5 == 0:
        print("Yes")
        return
    print("No")

main()