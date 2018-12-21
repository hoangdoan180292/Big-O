# https://www.hackerearth.com/practice/data-structures/trees/heapspriority-queues/practice-problems/algorithm/monk-and-multiplication/?fbclid=IwAR2gBWYYlm1xdEvYe-sOwgnFRrPufBWgskXuKTsVxSyqBaxeUEOfiXVYlUU
# Monk and Multiplication

import heapq

class PQEntry:
  def __init__(self, value):
    self.value = value
  def __lt__(self, other):
    return self.value > other.value

if __name__ == '__main__':
  n = int(input())
  a = raw_input().split(' ')
  h = []

  for i in range(len(a)):
    heapq.heappush(h, PQEntry(int(a[i])))

    if i < 2:
      print(-1)
    else:
      max1 = heapq.heappop(h)
      max2 = heapq.heappop(h)
      max3 = heapq.heappop(h)
      print(max1.value * max2.value * max3.value)
      heapq.heappush(h, max1)
      heapq.heappush(h, max2)
      heapq.heappush(h, max3)