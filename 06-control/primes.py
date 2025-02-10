
def range_inf(start):
    i = start
    while True:
        yield i
        i = i+1

def is_divisible_by_any(divisors, n):
    for divisor in divisors:
        if n % divisor == 0:
            return True
    return False

def primes():
    ps = []
    for i in range_inf(2):
        if not is_divisible_by_any(ps,i):
            ps.append(i)
            yield i


for p in primes():
    if p > 10000:
        break
print(p)
