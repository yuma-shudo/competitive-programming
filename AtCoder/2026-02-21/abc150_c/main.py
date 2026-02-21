import sys
input = sys.stdin.readline
from itertools import permutations

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))

    perm_search = []
    for perm in permutations(p, n):
        perm_search.append(int("".join(map(str, perm))))
    perm_search.sort()
    
    def bisect(x, sorted_list):
        low = 0
        high = len(sorted_list)-1

        while low < high:
            mid = (low+high)//2
            if x <= sorted_list[mid]:
                high = mid 
            else:
                low = mid+1
        
        return low
    
    a = bisect(int("".join(map(str, p))), perm_search)
    b = bisect(int("".join(map(str, q))), perm_search)
    print(abs(a-b))

from bisect import bisect_left
def main2():
    n = int(input())
    p = tuple(map(int, input().split()))
    q = tuple(map(int, input().split()))

    perms = sorted(permutations(range(1, n+1)))
    
    a = bisect_left(perms, p)
    b = bisect_left(perms, q)
    print(abs(a-b))

main()