# https://www.urionlinejudge.com.br/judge/en/problems/view/1610
# Dudu Service Maker

MAX = 10005
visited = [False] * MAX
inPath = [False] * MAX
graph = [[] for _ in range(MAX)]

def DFS(u):
  visited[u] = True
  inPath[u] = True

  for v in graph[u]:
    if visited[v]:
      if inPath[v]:
        return True
    else:
      if DFS(v):
        return True
  
  inPath[u] = False
  return False

T = int(input())

for _ in range(T):
  N, M = map(int, input().split())

  for i in range(N + 1):
    graph[i].clear()
    visited[i] = False
    inPath[i] = False
  
  for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
  
  isCyclic = False

  for i in range(1, N + 1):
    if not visited[i]:
      isCyclic = DFS(i)
      if isCyclic:
        break
  
  print("SIM" if isCyclic else "NAO")