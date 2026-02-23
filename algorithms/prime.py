def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # √nまで試し割り
        if n % i == 0:
            return False
    return True

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [i for i in range(n+1) if is_prime[i]]

def factorize(n):
    factors = {}
    d = 2
    while d * d <= n:       # √nまで試し割り
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:               # 残った数は素数
        factors[n] = factors.get(n, 0) + 1
    return factors