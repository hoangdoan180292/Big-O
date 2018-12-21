# 1074 – Extended Traffic

MAX = 100
INF = int(1e9)

class Edge:
  def __init__(self, source, target, weight):
    self.source = source
    self.target = target
    self.weight = weight

dist = []
graph = []
path = []

def BellmanFord(s):
  global dist
  global graph
  global path

  dist[s] = 0
  for i in range(1, n):
    for j in range(m):
      u = graph[j].source
      v = graph[j].target
      w = graph[j].weight
      if dist[u] != INF and dist[u] + w < dist[v]:
        dist[v] = dist[u] + w
        path[v] = u

  for i in range(m):
    u = graph[i].source
    v = graph[i].target
    w = graph[i].weight
    if dist[u] != INF and dist[u] + w < dist[v]:
      return False
  return True

if __name__ == '__main__':
  k = int(input()) # 5
  a = [0] + list(map(int, input().split())) # 6 7 8 9 10
  l = int(input()) # 6

  for _ in range(l):
    # 1 2
    # 2 3
    # 3 4
    # 1 5
    # 5 4
    # 4 5
    u, v = map(int, input().split())
    w = pow((a[v] - a[u]), 3)
    graph.append(Edge(u, v, w))