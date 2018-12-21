# https://www.spoj.com/problems/SHPATH/en/
# SHPATH - The Shortest Path

import queue

def inp():
  return map(int, input().split(' '))

class node:
  u = id
  dist = 0
  def __init__(self, u, val):
    self.id = u
    self.dist = val
  def __lt__(self, other):
    return self.dist <= other.dist

def dijkstra(src, des, graph):
  n = len(graph)
  pq = queue.PriorityQueue()
  pq.put(node(src, 0))
  dist = [10**9] * n
  dist[src] = 0
  while not pq.empty():
    top = pq.get()
    u = top.id
    d = top.dist
    if u == des:
      return d
    for neighbor in graph[u]:
      if d + neighbor.dist < dist[neighbor.id]:
        dist[neighbor.id] = d + neighbor.dist
        pq.put(node(neighbor.id, dist[neighbor.id]))

def solve():
  testcase = int(input())
  for t in range(testcase):
    n = int(input())
    graph = [[] for i in range(n)]
    pos = {}
    for i in range(n):
      name = input()
      pos[name] = i
      m = int(input())
      for j in range(m):
        u, val = inp()
        u-=1
        graph[i].append(node(u, val))
    q = int(input())
    for i in range(q):
      name1, name2 = input().split(' ')
      u = pos[name1]
      v = pos[name2]
      print(dijkstra(u, v, graph))

solve()