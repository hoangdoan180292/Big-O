#!/bin/python3

import math
import os
import random
import re
import sys
import queue

# Complete the bfs function below.
def bfs(n, m, graph, s):
  dist = [-1 for _ in range(n+1)]
  visited = [False for _ in range(n+1)]
  q = queue.Queue()
  q.put(s)
  dist[s] = 0
  visited[s] = True
  while q.empty() == False:
    u = q.get()
    for v in graph[u]:
      if visited[v] == False:
        visited[v] = True
        q.put(v)
        dist[v] = dist[u] + 1
  res = []
  for j in range(len(dist)):
    if j != s and j != 0:
      if dist[j] == -1:
        res.append(-1)
      else:
        res.append(dist[j] * 6)

  return res

if __name__ == '__main__':
  results = []

  q = int(input())

  for q_itr in range(q):
    n, m = map(int, input().split())
    graph = [[] for i in range(n + 1)]
    for _ in range(m):
      u, v = map(int, input().split())
      graph[u].append(v)
      graph[v].append(u)

    s = int(input())

    results.append(bfs(n, m, graph, s))

  for result in results:
    print(' '.join(map(str, result)))