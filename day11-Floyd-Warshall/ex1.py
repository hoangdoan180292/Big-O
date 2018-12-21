# import queue
# MAX = 100
# INF = int(1e9)

# def printPath(s, t):
#   b = []
#   while  s != t:
#     b.append(t)
#     t = path[s][t]
#   b.append(s)
#   for i in range(len(b) - 1, -1, -1):
#     print(b[i], end= '' if i > 0 else '\n')

# def FloydWarshall(graph, dist):
#   for i in range(V):
#     for j in range(V):
#       dist[i][j] = graph[i][j]
#       if graph[i][j] != INF and i != j:
#         path[i][j] = i
#       else:
#         path[i][j] = -1
#   for k in range(V):
#     for i in range(V):
#       for j in range(V):
#         if dist[i][j] > dist[i][k] + dist[k][j]:
#           dist[i][j] = dist[i][k] + dist[k][j]
#           path[i][j] = path[k][j]
#   for i in range(V):
#     if dist[i][i] < 0:
#       return False
#   return True

# if __name__ == '__main__':
#   v = int(intput())
#   graph = [[None for i in range(V)] for j in range(V)]
#   dist = [[None for i in range(V)] for j in range(V)]
#   path = [[None for i in range(V)] for j in range(V)]
#   for i in range(V):
#     line = list(map(int, input().split()))
#     for j in range(V):
#       graph[i][j] = INF if line[j] == 0 and i != j else line[j]

#   FloydWarshall(graph, dist)
#   s, t = 0,4
#   printPath(s, t)
#   print(dist[s][t])

# NYN
# YNN
# NYN
# 0 1

if __name__ == '__main__':
  n = int(input())
  for _ in range(n):
    V = input()
    l = len(V)

    graph = [[None for i in range(l)] for j in range(l)]
    dist = [[None for i in range(l)] for j in range(l)]
    path = [[None for i in range(l)] for j in range(l)]

    for j in range(l):
      graph[0][j] = V[j]
    for i in range(l - 1):
      x = input()
      for j in range(len(x)):
        graph[i+1][j] = x[j]

    print(graph)
    print('-------------')