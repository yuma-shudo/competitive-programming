import sys
input = sys.stdin.readline

def main():
    n, w = map(int, input().split())
    needs = [0]*(2*(10**5)+1)
    for _ in range(n):
        s, t, p = map(int, input().split())
        needs[s] += p
        needs[t] -= p
    
    if needs[0] > w:
        print("No")
        return
    for i in range(2*(10**5)):
        need = needs[i]+needs[i+1]
        if need > w:
            print("No")
            return
        needs[i+1] = need
    print("Yes")
    return

def main2():
    n, w = map(int, input().split())

    events = []
    max_t = 0
    for _ in range(n):
        s, t, p = map(int, input().split())
        events.append((s, t, p))
        max_t = max(max_t, t)

    diff = [0] * (max_t + 2)
    for s, t, p in events:
        diff[s] += p
        diff[t] -= p

    current = 0
    for i in range(max_t + 1):
        current += diff[i]
        if current > w:
            print("No")
            return
        
    print("Yes")

main()