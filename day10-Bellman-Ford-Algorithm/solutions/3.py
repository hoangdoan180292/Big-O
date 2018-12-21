# https://www.urionlinejudge.com.br/judge/en/problems/view/1655
# 106 Miles To Chicago

def inp():
  return map(int, input().split(' '))

class node:
  u = 0
  v = 0
  val = 0
  def __init__(self, u, v, val):
    self.u = u
    self.v = v
    self.val = val

def FBM(n, m, graph):
  dist = [10**9] * n
  dist[0] = 0
  for i in range(n-1):
    for edge in graph:
      u = edge.u
      v = edge.v
      val = edge.val
      if dist[u] != 10**9 and dist[u] + val < dist[v]:
        dist[v] = dist[u] + val
  for edge in graph:
    u = edge.u
    v = edge.v
    val = edge.val
    if dist[u] != 10**9 and dist[u] + val < dist[v]:
      return True # have cycle
  return False

def solve():
  while True:
    line = list(inp())
    if len(line) == 1:
      break
    n = line[0]
    m = line[1]
    graph = []

    for i in range(m):
      u, v, val = inp()
      u-=1
      v-=1
      graph.append(node(u, v, val/100.0))

    pro = [-1.5] * n
    pro[0] = 1.0
    for s in range(n-1):
      for edge in graph:
        u = edge.u
        v = edge.v
        val = edge.val
        pro[u] = max(pro[u], pro[v] * val)
        pro[v] = max(pro[v], pro[u] * val)
    print("{:.6f} percent".format(pro[n-1] * 100.0))

solve()