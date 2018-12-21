# https://www.spoj.com/problems/MICEMAZE/fbclid=IwAR1V9Y9hLFaFLJsEI9clI7uD2n_LdUtwIjAMN89ObMUrTMiaT_SjJ0iOPTQ
# MICEMAZE - Mice and Maze

# 4 (N <= 100)
# 2 (Exit)
# 1 (Thoi gian)

import queue
INF = int(1e9)

class Node:
  def __init__(self, id, dist):
    self.dist = dist
    self.id = id
  def __lt__(self, other):
    return self.dist <= other.dist

def Dijkstra(s, count):
  pq = queue.PriorityQueue()
  pq.put(Node(s, 0))
  dist[s] = 0
  time = 0
  if s != E:
    while pq.empty() == False:
      top = pq.get()
      u = top.id
      w = top.dist
      for neighbor in graph[u]:
        if neighbor.id == E:
          time = w + neighbor.dist
          break
        dist[neighbor.id] = w + neighbor.dist
        pq.put(Node(neighbor.id, dist[neighbor.id]))
  if time < 2:
    count += 1
  return count

N = int(input())
E = int(input())
T = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
dist  = [INF for _ in range(N+1)]
path  = [-1 for _ in range(N+1)]
count = 0

for i in range(M):
  a, b, t = list(map(int, input().split()))
  graph[a].append(Node(b, t))
  graph[b].append(Node(a, t))

for x in range(N):
  print(Dijkstra(x, count))