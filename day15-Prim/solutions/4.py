# https://www.spoj.com/problems/MST/
# MST - Minimum Spanning Tree

import queue

class node:
  dist = 0
  index = 0

  def __init__(self, dist, index):
    self.dist = dist
    self.index = index

  def __lt__(self, other):
    return self.dist < other.dist

def inp():
  return map(int, input().split())

def prim(graph, src):
  n = len(graph)
  dist = [1e18 for i in range(n)]
  visited = [0 for i in range(n)]
  total_cost = 0
  dist[src] = 0
  Q = queue.PriorityQueue()
  Q.put(node(0, src))

  while not Q.empty():
    temp = Q.get()
    u = temp.index
    visited[u] = True
    for item in graph[u]:
      v = item.index
      if not visited[v] and dist[v] > item.dist:
        dist[v] = item.dist
        Q.put(node(dist[v], v))
  for i in range(n):
    total_cost += dist[i]
  return total_cost

def solve():
  n, m = inp()
  graph = [[] for i in range(n)]
  for i in range(m):
    u, v, val = inp()
    u -= 1
    v -= 1
    graph[u].append(node(val, v))
    graph[v].append(node(val, u))
  print(prim(graph, 0))

solve()