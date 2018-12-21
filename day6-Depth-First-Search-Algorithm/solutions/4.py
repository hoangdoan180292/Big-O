# https://codeforces.com/problemset/problem/723/D
# D. Lakes in Berland

import threading
import sys
def inp():
  return map(int, input().split(' '))

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
global cnt

class node():
  count = 0
  x = 0
  y = 0
  def __init__(self, count, x, y):
    self.x = x
    self.y = y
    self.count = count

def checkCell(s, x, y):
  return x >= 0 and y >= 0 and x < len(s) and y < len(s[0]) and s[x][y] == '.'

def DFS(x, y, s, used):
  used[x][y] = True
  global cnt
  cnt += 1
  for d in range(4):
    xx = x + dx[d]
    yy = y + dy[d]
    if not checkCell(s, xx, yy):
      continue
    if used[xx][yy]:
      continue
    DFS(xx, yy, s, used)

def DFS2(s, x, y):
  s[x][y] = '*'
  for d in range(4):
    xx = x + dx[d]
    yy = y + dy[d]
    if not checkCell(s, xx, yy):
      continue
    DFS2(s, xx, yy)

def solve():
  n, m, k = inp()
  s = []
  a = []
  global cnt
  cnt = 0
  for i in range(n):
    s.append(list(input()))
  used = [[False for y in range(m)] for x in range(n)]
  for i in range(n):
    for j in range(m):
      if i > 0 and i < n - 1 and j > 0 and j < m - 1:
        continue
      if s[i][j] == '*':
        continue
      DFS(i, j, s, used)

  for i in range(n):
    for j in range(m):
      if s[i][j] == '*':
        continue
      if used[i][j]:
        continue
      cnt = 0
      DFS(i, j, s, used)
      a.append(node(cnt, i, j))
  a = sorted(a, key=lambda node: node.count, reverse=True)
  sz = len(a)
  sum = 0
  for i in range(k, sz):
    sum += a[i].count
    DFS2(s, a[i].x, a[i].y)
  print(sum)
  for i in range(n):
    print(''.join(s[i]))

if __name__ == '__main__':
  # initation stack size is not enough, you must increase it
  threading.stack_size(67108864)
  sys.setrecursionlimit(2**20)
  thread = threading.Thread(target=solve)
  thread.start()