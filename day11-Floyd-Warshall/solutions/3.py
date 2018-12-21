# https://www.spoj.com/problems/ARBITRAG/
# ARBITRAG - Arbitrage

dist = []
currencies = []

def findCurrency(s):
  global currencies
  for i in range(n):
    if currencies[i] == s:
      return i;
  return -1;

def FloydWarshall():
  global dist
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if dist[i][j] < dist[i][k] * dist[k][j]:
          dist[i][j] = dist[i][k] * dist[k][j]

tc = 1
while True:
  n = int(input())
  if n == 0:
    break
  dist = [[0.0 for i in range(n)] for j in range(n)]
  currencies = []
  for i in range(n):
    dist[i][i] = 1.0
    currencies.append(input())
  m = int(input())
  for i in range(m):
    u, w, v = input().split()
    dist[findCurrency(u)][findCurrency(v)] = float(w)
  FloydWarshall()
  flag = False
  for i in range(n):
    if dist[i][i] > 1.0:
      flag = True
      break
  print("Case {}: {}".format(tc, "Yes" if flag else "No"))
  tc += 1
  input()