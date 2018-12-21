# https://uva.onlinejudge.org/index.php?Itemid=8&category=316&option=com_onlinejudge&page=show_problem&problem=1552
# 10611 - The Playboy Chimp

import sys

def inp():
  return map(int, input().split())

def solve():
  n = int(input())
  a = list(inp())

  q = int(input())
  query = list(inp())
  for x in query:
    pos = -1
    l = 0
    r = n-1
    while l <= r:
      mid = int( (l + r) / 2 )
      if a[mid] < x:
        pos = max(pos, mid)
        l = mid + 1
      else:
        r = mid - 1
    if pos == -1:
        ans = "X"
    else:
      ans = str(a[pos])

    pos = n
    l = 0
    r = n - 1
    while l <= r:
      mid = int( (l + r) / 2)
      if a[mid] > x:
        pos = min(pos, mid)
        r = mid - 1
      else:
        l = mid + 1
    if pos == n:
      ans += " X"
    else:
      ans += " " + str(a[pos])

    print(ans)

solve()