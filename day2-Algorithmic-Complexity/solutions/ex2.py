# https://codeforces.com/problemset/problem/387/B
# B. George and Round

def inp():
    return map(int, input().split())

n, m = inp()
a = list(inp())
b = list(inp())

count = 0
j = 0

for i in range(n):
  while j < m:
    if b[j] >= a[i]:
      count += 1
      j += 1
      break
    else:
      j += 1

print(n - count)