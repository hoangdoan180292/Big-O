# http://lightoj.com/volume_showproblem.php?problem=1041
# 1041 - Road Construction

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
    if dist[i] >= 1e18:
      return "Impossible"
    total_cost += dist[i]
  return total_cost

def solve():
  testcase = int(input())
  for t in range(testcase):
    input()
    m = int(input())
    cities = dict()
    cnt = 0
    graph = []
    for i in range(m):
      name1, name2, cost = input().split()
      if name1 in cities:
        u = cities[name1]
      else:
        u = cnt
        cities[name1] = cnt
        graph.append([])
        cnt+=1
      if name2 in cities:
        v = cities[name2]
      else:
        v = cnt
        cities[name2] = cnt
        graph.append([])
        cnt+=1
      cost = int(cost)
      graph[u].append(node(cost, v))
      graph[v].append(node(cost, u))

    print("Case {}: {}".format(t + 1, prim(graph, 0)))

solve()