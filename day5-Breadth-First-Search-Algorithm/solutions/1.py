# https://www.hackerrank.com/challenges/bfsshortreach/problem
# Breadth First Search: Shortest Reach

import queue

MAX = 1000 + 5
visited = [False] * MAX
dist = [0] * MAX
graph = [[] for i in range(MAX)]

def BFS(s):
  q = queue.Queue()
  visited[s] = True
  q.put(s)

  while not q.empty():
    u = q.get()

    for v in graph[u]:
      if not visited[v]:
        visited[v] = True
        dist[v] = dist[u] + 1
        q.put(v)

Q = int(input())

for _ in range(Q):
  V, E = map(int, input().split())

  for i in range(MAX):
    graph[i].clear()
    visited[i] = False
    dist[i] = 0
  
  for i in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
  
  s = int(input())
  BFS(s)

  for i in range(1, V + 1):
    if i == s:
      continue

    print(dist[i] * 6 if visited[i] else -1, end=' ')
  
  print()