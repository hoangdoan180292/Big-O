# https://www.spoj.com/problems/OPCPIZZA/
# OPCPIZZA - Pizzamania

import sys

def BS_search(a, l, r, value):
  while l <= r:
    mid = (l + r) // 2
    if a[mid] == value:
      return True
    if a[mid] > value:
      r = mid - 1
    else:
      l = mid + 1
  return False

def solve():
  testcase = int(input())
  for t in range(testcase):
    n, m = map(int, input().split())
    a = list(map(int, input().split())) 
    a.sort()
    ans = 0
    for x in a:
      y = m - x
      if x != y:
        if BS_search(a, 0, n-1, y):
          ans+=1
    print(ans//2)

solve()