# https://uva.onlinejudge.org/index.php?Itemid=8&option=com_onlinejudge&page=show_problem&problem=1498
# 10557 - XYZZY

import queue
import threading
import sys

def inp():
  return map(int, input().split())

class node:
  u = 0
  v = 0
  def __init__(self, u, v):
    self.u = u
    self.v = v

def canReach(src, des, graph): # BFS
  q = queue.Queue()
  q.put(src)
  n = des + 1
  visited = [False] * n
  visited[src] = True
  if src == des:
    return True
  while not q.empty():
    u = q.get()
    for edge in graph:
      if edge.u == u and not visited[edge.v]:
        visited[edge.v] = True
        if edge.v == des:
          return True
        q.put(edge.v)

  return False

def FBM(n, m, graph, en):
  dist = [-10**9] * n
  dist[0] = 100
  for i in range(n-1):
    for edge in graph:
      u = edge.u
      v = edge.v
      if dist[u] <= 0:
        continue
      if dist[u] + en[v] > dist[v]:
        dist[v] = dist[u] + en[v]
  for edge in graph:
    u = edge.u
    v = edge.v
    if dist[u] <= 0:
      continue
    # print (str(u) + ' ' + str(v)  + " " + str(dist[u] + en[v]) + " " + str(dist[v]))
    if dist[u] + en[v] > dist[v] and canReach(u, n-1, graph):
      return True # have cycle

  return dist[n-1] > 0 or False

def solve():
  while True:
    n = int(input())
    if n == -1:
      break
    graph = []
    en = [0] * n
    for i in range(n):
      line = list(inp())
      en[i] = line[0]
      if (len(line) == 1):
        line.extend(list(map(int, input().split())))
      while (len(line) != line[1] + 2):
        line.extend(list(map(int, input().split())))
      # if (len(line) != line[1] + 2):
      #     while True:
      #         en[i] = line[0]
      for j in line[2:]:
          graph.append(node(i, j - 1))
      # print(line)
    canGo = FBM(n, len(graph), graph, en)
    if canGo:
      print("winnable")
    else:
      print("hopeless")

if __name__ == '__main__':
  solve()