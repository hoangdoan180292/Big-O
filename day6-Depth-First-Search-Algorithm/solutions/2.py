# https://www.spoj.com/problems/CAM5/
# CAM5 - prayatna PR

import queue

def DFS(src):
  # using stack
  s = queue.LifoQueue()
  s.put(src)
  visited[src] = True
  while not s.empty():
    u = s.get()
    for v in graph[u]:
      if not visited[v]:
        visited[v] = True
        s.put(v)

if __name__ == '__main__':
  line = ''
  while line == '':
    line = input().strip()
  tcase = int(line)
  while tcase > 0:
    line = ''
    while line == '':
      line = input().strip()
    V = int(line)
    E = int(input())
    graph = [[] for i in range(V)]
    visited = [False] * V
    for i in range(E):
      u, v = map(int, input().split())
      graph[u].append(v)
      graph[v].append(u)
    count = 0
    for i in range(V):
      if not visited[i]:
        count+=1
        DFS(i)
    print(count)
    tcase-=1