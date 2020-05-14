def is_prime(n):
    if n < 3 or n % 2 == 0:
        return n == 2
    else:
        return not any(n % i == 0 for i in range(3, int(n **0.5 + 2), 2))

def get_prime_factors(n):
    prime_factors= []
    d = 2
    while d * d <= n:
        while n % d == 0:
            n //=3
            prime_factors.append(d)
        d+=1
    if n > 1:
        assert d <= n
        prime_factors.append(n)
    return prime_factors
