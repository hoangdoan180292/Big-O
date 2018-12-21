# https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/dhoom-4/description/
# Dhoom 4

import queue

def inp():
  return map(int, input().split(' '))

def BFS(start, end):
  q = queue.Queue()
  q.put(start)
  path = [-1 for x in range(100005)]
  path[start] = 0
  while not q.empty():
    u = q.get()
    for i in range(n):
      value = a[i] * u
      value %= 100000
      if path[value] == -1:
        path[value] = path[u] + 1
        q.put(value)
        if value == end:
          return path[end]
  return -1;

if __name__ == '__main__':
  s, d = inp()
  n = int(input())
  a = list(inp())
  print(BFS(s, d))