# https://uva.onlinejudge.org/index.php?Itemid=8&option=com_onlinejudge&page=show_problem&problem=499
# 558 - Wormholes

def inp():
  return map(int, input().split(' '))

class node:
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
  tcase = int(input())
  for t in range(tcase):
    graph = []
    n, m = inp()
    for i in range(m):
      u, v, val = inp()
      graph.append(node(u, v, val))
    cycle = FBM(n, m, graph)
    if cycle:
      print("possible")
    else:
      print("not possible")

solve()