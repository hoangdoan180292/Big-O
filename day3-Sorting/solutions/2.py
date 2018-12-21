# https://codeforces.com/problemset/problem/451/B
# B. Sort the Array

n = int(input()) 
a = list(map(int, input().split()))

b = sorted(a)
l = -1
r = -1 

for i in range(n): 
  if (a[i] != b[i] and l == -1): 
    l = i 
  if (a[i] != b[i]):
    r = i 
        
if (l == -1 and r == -1): 
  l = 0 
  r = 0 

u = l 
v = r 

while (u < v): 
  a[u], a[v] = a[v], a[u]
  u += 1 
  v -= 1 

for i in range(n): 
  if (a[i] != b[i]):
    print("no") 
    exit()


print("yes")     
print(str(l + 1) + ' ' + str(r + 1)) 