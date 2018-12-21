# https://codeforces.com/problemset/problem/557/B
# B. Pasha and Tea

n, w = map(int, input().split(' '))
v = list(map(int, input().split(' ')))

v = sorted(v) 
if v[n] / v[0] >= 2:
  x = v[0] 
else:
  x = v[n] / 2

sum = 3 * n * x 

if (sum > w):
  sum = w 

print(sum)