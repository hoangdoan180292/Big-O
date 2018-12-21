# https://codeforces.com/problemset/problem/161/A
# A. Dress'em in Vests!

def inp():
  return map(int, input().split())

n, m, x, y = inp()
a = list(inp())
b = list(inp())

V = []
j = 0

for i in range(m):
  while j < n and a[j] + y < b[i]:
    j += 1 

  if j == n:
    break
  
  if a[j] - x <= b[i] <= a[j] + y:
    V += [[j + 1, i + 1]]
    j += 1
    
print(len(V))
for x in V:
  print(x[0], x[1])