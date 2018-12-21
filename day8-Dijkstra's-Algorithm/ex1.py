import queue
INF = int(1e9)

class Node:
  def __init__(self, id, dist):
    self.dist = dist
    self.id = id
  def __lt__(self, other):
    return self.dist <= other.dist

def Dijkstra(s):
  pq = queue.PriorityQueue()
  pq.put(Node(s, 0))
  dist[s] = 0
  while pq.empty() == False:
    top = pq.get()
    u = top.id
    w = top.dist
    for neighbor in graph[u]:
      if w + neighbor.dist < dist[neighbor.id]:
        dist[neighbor.id] = w + neighbor.dist
        pq.put(Node(neighbor.id, dist[neighbor.id]))
        path[neighbor.id] = u

N     = int(input())
graph = [[] for _ in range(501)]
dist  = [INF for _ in range(501)]
path  = [-1 for _ in range(501)]
d     = []

for i in range(N):
  A, B, W = list(map(int, input().split()))
  graph[A].append(Node(B, W))
  graph[B].append(Node(A, W))
U = int(input())
Q = int(input())

Dijkstra(U)

for i in range(Q):
  V = int(input())
  if dist[V] == INF:
    print('NO PATH')
  else:
    print(dist[V])
