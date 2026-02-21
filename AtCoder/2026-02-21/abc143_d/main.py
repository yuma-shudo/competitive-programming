import sys
input = sys.stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))

    l.sort()
    ans = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            current = l[i] + l[j]
            low = j+1
            high = n
            while low<high:
                mid = (low+high)//2
                if l[mid] >= current:
                    high = mid
                else:
                    low = mid + 1
            ans += max(0, high - (j+1))
    print(ans)

main()