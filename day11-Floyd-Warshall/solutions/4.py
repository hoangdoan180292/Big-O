# https://uva.onlinejudge.org/index.php?Itemid=8&option=com_onlinejudge&page=show_problem&problem=1112
# 10171 - Meeting Prof. Miguel...

MAX = 28
INF = 10 ** 9
def floyd_warshal(dist):
  for k in range(MAX):
    for i in range(MAX):
      for j in range(MAX):
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
while True:
  n = int(input())
  if n == 0:
    break
  
  SMD = [[INF if j != i else 0 for j in range(MAX)] for i in range(MAX)]
  MGD = [[INF if j != i else 0 for j in range(MAX)] for i in range(MAX)]
  
  for i in range(n):
    a, d, x, y, w = input().split()
    x = ord(x) - 64
    y = ord(y) - 64
    w = int(w)

    if a == 'Y':
      if SMD[x][y] > w:
        SMD[x][y] = w
        if d == 'B':
          if SMD[y][x] > w:
            SMD[y][x] = w
    else:
      if MGD[x][y] > w:
        MGD[x][y] = w
      if d == 'B':
        if MGD[y][x] > w:
          MGD[y][x] = w
        
  x, y = map(lambda x: ord(x) - 64, input().split())
  floyd_warshal(SMD)
  floyd_warshal(MGD)

  ans = []
  for i in range(1, MAX):
    d1 = SMD[x][i]
    d2 = MGD[y][i]
    if d1 != INF and d2 != INF:
      ans.append((d1 + d2, i))

  if len(ans) == 0:
    print('You will never meet.')
    continue
  ans.sort()
  for i in range(len(ans)):
    if i == 0:
      print(ans[i][0], end = '')
    if ans[i][0] == ans[0][0]:
      print(' ' +  chr(ans[i][1] + 64), end = '')
  print()