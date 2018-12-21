# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1895
# 10954 - Add All

import queue
import sys
import threading

def solve():
  while True:
    n = int(input().strip())
    if n == 0:
      break
    pq = queue.PriorityQueue()
    ans = 0
    a = list(map(int, input().strip().split()))
    for x in a:
      pq.put(x)
    while pq.qsize() > 1:
      x = pq.get()
      y = pq.get()
      ans += x + y
      pq.put(x + y)
    print(ans)

solve()