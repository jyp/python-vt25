# python pythagorean.py  2.13s user 0.02s system 99% cpu 2.159 total (testing all triples)
# python pythagorean.py  1.17s user 0.02s system 99% cpu 1.195 total (a ≤ b)
# python pythagorean.py  0.41s user 0.01s system 98% cpu 0.428 total (b ≤ c)

n = 300
# consider a,b,c natural numbers up to n-1

result = []
for a in range(1,n):
    for b in range(a,n):
        for c in range(b,n):
            if a*a + b*b == c*c:
                result.append((a,b,c))
print(result)
print(len(result))
