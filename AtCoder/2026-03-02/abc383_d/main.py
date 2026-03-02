import sys
input = sys.stdin.readline
from bisect import bisect_right

def main():
    n = int(input())
    sqrt_n = int(n**0.5)
    if sqrt_n < 6:
        print(0)
        exit()

    def sieve(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n+1, i):
                    is_prime[j] = False
        return [i for i in range(n+1) if is_prime[i]]

    primes = sieve(sqrt_n//2)
    two_primes = []
    for i in range(len(primes)-1):
        for j in range(i+1, len(primes)):
            two_prime = primes[i]*primes[j]
            if two_prime>sqrt_n:
                break
            two_primes.append(two_prime)
    for i in range(len(primes)):
        two_prime = primes[i]**4
        if two_prime>sqrt_n:
            break
        two_primes.append(two_prime)
    two_primes.sort()
    ans = bisect_right(two_primes, sqrt_n)

    print(ans)



main()