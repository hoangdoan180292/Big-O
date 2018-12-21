import queue

INF = 1e9

class Node:
  def __init__(self, id, dist):
    self.dist = dist
    self.id = id

  def __lt__(self, other):
    return self.dist <= other.dist

def Prim(src):
  pq = queue.PriorityQueue()
  pq.put(Node(src, 0))
  dist[src] = 0
  while pq.empty() == False:
    top = pq.get()
    u = top.id
    d = top.dist
    visited[u] = True
    for neighbor in graph[u]:
      v = neighbor.id
      w = neighbor.dist
      if visited[v] == False and w < dist[v]:
        dist[v] = w
        pq.put(Node(v, w))
        path[v] = u

def printMST():
  ans = 0
  for i in range(n+1):
    if path[i] == -1:
      continue
    ans += dist[i]
  print(ans)
  # print("Weight of MST: {0}".format(ans))

if __name__ == '__main__':
  n, m = map(int, input().split())
  graph = [[] for _ in range(n+1)]
  dist = [INF for _ in range(n+1)]
  path = [-1 for _ in range(n+1)]
  visited = [False for _ in range(n+1)]
  for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append(Node(v, w))
    graph[v].append(Node(u, w))
  Prim(1)
  printMST()