# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1498
# 10557 - XYZZY

# while True:
#   N = int(input())
#   if N == -1:
#     break
#   graph = zeros((N + 1, N + 1), dtype=int)
#   for i in range(1, N + 1):
#     line = map(int, raw_input().split())
#     graph[i, 0] = line[0]
#     if line[1] > 0:
#       for j in line[2:]:
#         graph[i, j] = 1
#   energy = [0] * (N + 1)
#   q = deque([(1, 100)])
#   while q:
#     v1, e = q.popleft()
#     if energy[v1] > 100 * N and e > energy[v1]:
#       continue

#     if e > energy[v1]:
#       energy[v1] = e
#       for v2 in range(1, N + 1):
#         if graph[v1, v2]:
#           q.append((v2, e + graph[v2, 0]))
#   if energy[N] != 0:
#     print('winnable')
#   else:
#    print('hopeless')

input n

for u 1 -> n:
  input e[u]
  input n_u
  for j 1 -> n_u:
    input v
    edges.push((u, v))
    graph[u].push(v)

Bellman():
  ene[1] = 100
  for i 0 -> n - 1:
    for (u, v) thuoc edges:
      if ene[u] > 0 && ene[u] + ene[v] > ene[v]:
        ene[v] = ene[u] + ene[v]
  if ene[n] > 0:
    return true

  for (u, v) thuoc edges:
    if ene[u] > 0 && ene[v]:
      if DFS(u, n, graph) == True:
        return true
  return false

if Bellman