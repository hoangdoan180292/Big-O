# https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/bishu-and-his-girlfriend/
# Bishu and his Girlfriend

n = int(input())
graph = [[] for i in range(n)]
for i in range(n - 1):
  u, v = map(int, input().split())
  graph[u - 1].append(v - 1)
  graph[v - 1].append(u - 1)

def dfs(src):
  stack = [src]
  visited = [False] * n
  visited[src] = True
  dist = [0] * n
  while len(stack):
    u = stack.pop()
    if u == 0:
      return dist[u]
    for v in graph[u]:
      if not visited[v]:
        visited[v] = True
        dist[v] = dist[u] + 1
        stack.append(v)

q = int(input())
bestId = -1
bestDist = n + 1
for i in range(q):
  id = int(input()) - 1
  dist = dfs(id)
  if dist < bestDist or (dist == bestDist and id < bestId):
    bestId = id
    bestDist = dist
print(bestId + 1)