import sys
input = sys.stdin.readline

def main():
    n, m, x = map(int, input().split())
    books = [tuple(map(int, input().split())) for _ in range(n)]
    skilled = []

    for i in range(1<<n):
        price = 0
        algorithms = [0]*m
        for j in range(n):
            if i>>j & 1:
                price += books[j][0]
                for k in range(m):
                    algorithms[k] += books[j][k+1]

        overSkill = True
        for k in range(m):
            if algorithms[k] < x:
                overSkill = False

        if overSkill:
            skilled.append(price)

    if skilled:
        print(min(skilled))
    else:
        print(-1)

def main2():
    n, m, x = map(int, input().split())
    books = [tuple(map(int, input().split())) for _ in range(n)]
    ans = float('inf')

    for i in range(1<<n):
        price = 0
        skills = [0]*m
        for j in range(n):
            if i>>j & 1:
                price += books[j][0]
                for k in range(m):
                    skills[k] += books[j][k+1]

        if all(s >= x for s in skills):
            ans = min(ans, price)

    print(ans if ans != float('inf') else -1)

main()