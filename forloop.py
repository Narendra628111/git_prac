def gcd(m,n):
    while(n):
        m,n=n,m%n
    return m
m=int(input())
n=int(input())
a=(gcd(m,n))
b=m*n//(a)
print(b)