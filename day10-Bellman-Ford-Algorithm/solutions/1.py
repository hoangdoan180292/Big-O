# http://www.lightoj.com/volume_showproblem.php?problem=1074

def inp():
    return map(int, raw_input().split(' '))

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
  return dist

def solve():
  tcase = int(input())
  for t in range(tcase):
    graph = []
    raw_input()
    n = int(input())
    a = list(inp())
    m = int(input())
    for i in range(m):
      u, v = inp()
      u-=1
      v-=1
      val = (a[v] - a[u])**3
      graph.append(node(u, v, val))
    dist = FBM(n, m, graph)
    query = int(input())
    ans = []
    for q in range(query):
      k = int(input()) - 1
      if dist[k] < 3:
        ans.append('?')
      else:
        ans.append(str(dist[k]))
    print("Case " + str(t + 1) + ":")
    print(' '.join(ans))

solve()