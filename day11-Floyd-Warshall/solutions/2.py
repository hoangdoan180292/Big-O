# https://uva.onlinejudge.org/index.php?Itemid=8&option=com_onlinejudge&page=show_problem&problem=508
# 567 - Risk

import sys

def solve():
  for tc in range(1, 1000000):
    try:
      n = 20
      graph = []
      for i in range(19):
        graph.append(list(map(int, input().split()))[1:])
      graph.append([])
      #FLOYD
      dist = [[10 ** 9] * n for i in range(n)]
      for u in range(n):
        for v in graph[u]:
            dist[u][v-1] = dist[v - 1][u] = 1
      for i in range(n):
        dist[i][i] = 0

      for k in range(n):
        for i in range(n):
          for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
              dist[i][j] = dist[i][k] + dist[k][j]
      print ("Test Set #" + str(tc))
      q = int(input())
      for i in range(q):
        u, v = map(int, input().split())
        print('%2d to %2d: %d' % (u, v, dist[u - 1][v - 1]))
      print()
    except EOFError:
      break
solve()