# https://www.spoj.com/problems/MICEMAZE/
# MICEMAZE - Mice and Maze

import queue

MAX = 500
INF = int(1e9)

# khai báo class Node với id là tên đỉnh, dist là chi phí
# define operator __lt__ (less than) cho class, so sánh theo dist nhỏ hơn, dùng trong PriorityQueue
class Node:
  dist = 0
  id = 0
  def __init__(self, id, dist):
    self.dist = dist
    self.id = id
  def __lt__(self, other):
    return self.dist <= other.dist

def Dijkstra(s, graph, dist):
  pq = queue.PriorityQueue()
  pq.put(Node(s, 0))
  dist[s] = 0
  while pq.empty() == False:
    top = pq.get()
    node = top.id
    d = top.dist
    for neighbor in graph[node]:
      if d + neighbor.dist < dist[neighbor.id]:
        dist[neighbor.id] = d + neighbor.dist
        pq.put(Node(neighbor.id, dist[neighbor.id]))
        path[neighbor.id] = node

if __name__ == '__main__':
  n = int(input())
  s = int(input())
  t = int(input())
  graph = [[] for i in range(n+5)]
  dist = [INF for i in range(n+5)]
  path = [-1 for i in range(n+5)]
  m = int(input())
  for i in range(m):
    v, u, w = map(int, input().split())
    graph[u].append(Node(v, w))
  Dijkstra(s, graph, dist)
  cnt = 0
  for i in range(1, n+1, 1):
    cnt += 1 if dist[i] <= t else 0
  print(cnt)