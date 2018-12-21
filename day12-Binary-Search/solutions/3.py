# https://www.spoj.com/problems/EKO/
# EKO - Eko

import sys

def inp():
  return map(int, input().split(' '))

def check(a, x):
  sum = 0
  for item in a:
    sum += max(0, item - x)
  return sum

def BS_search(a, l, r, k):
  ans = r
  while l <= r:
    mid = int( (l + r) / 2 )
    if check(a, mid) >= k:
      ans = mid
      l = mid + 1
    else:
      r = mid - 1
  return ans

def solve():
  n, k = inp()
  a = list(inp())
  vmin = 0
  vmax = 1e9
  print (BS_search(a, vmin, vmax, k))

solve()