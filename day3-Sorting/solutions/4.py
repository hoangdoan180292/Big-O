# https://codeforces.com/problemset/problem/439/B
# B. Devu, the Dumb Guy

(n,x) = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
ans =  0
for i in range(0,n):
  ans+= a[i]*x
  if x > 1:
    x-=1
print(ans)
