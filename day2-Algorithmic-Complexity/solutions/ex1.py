# https://codeforces.com/problemset/problem/279/B
# B. Books

n, t = map(int, input().split())
a = list(map(int, input().split()))
 
j = 0 
count = 0 
books = 0
 
for i in range(n): 
  while t < a[i]: 
    t += a[j]
    j += 1 
    count -= 1

  t -= a[i] 
  count += 1

  books = max(books, count) 
 
print(books)