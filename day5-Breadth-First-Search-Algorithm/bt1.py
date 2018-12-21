#!/bin/python3
import queue
MAX = 100000

def bfs(n, m, k, graph):
  dist = [-1 for _ in range(MAX+1)]
  q = queue.Queue()
  q.put(n) # q = [3]
  dist[n] = 0 # [-1, -1, -1, 0, -1, ...]
  while q.empty() == False:
    u = q.get() # u = 3
    if u == m: # u = 3, m = 30
      break
    for i in range(k):
      tmp = (u*graph[i])%MAX
      if dist[tmp] == -1:
        dist[tmp] = dist[u] + 1
        q.put(tmp)
  return dist[m]

if __name__ == '__main__':
  n, m = map(int, input().split())
  k = int(input())
  graph = list(map(int, input().split()))
  print(bfs(n, m, k, graph))

# 3 30
# 3
# 2 5 7

# n = 3
# m = 30
# k = 3
# graph = [2, 5, 7]