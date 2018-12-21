# https://www.spoj.com/problems/SOCIALNE/
# SOCIALNE - Possible Friends

def solve():
  testcase = int(input())
  for test in range(testcase):
    matrix = []
    line = input()
    matrix.append(line)
    n = len(line)
    for i in range(n - 1):
      line = input()
      matrix.append(line)

    # FLOYD
    dist = [[1e9 for i in range(n)] for j in range (n)]
    for i in range(n):
      for j in range(n):
        if i == j:
          dist[i][j] = 0
        elif matrix[i][j] == 'Y':
          dist[i][j] = 1
        else:
          dist[i][j] = 1e9 #infinity
    for k in range(n):
      for i in range(n):
        for j in range(n):
          if dist[i][j] > dist[i][k] + dist[k][j]:
            dist[i][j] = dist[i][k] + dist[k][j]
    ans = 0
    index = 0
    for i in range(n):
      count = 0
      for j in range (n):
        if dist[i][j] == 2:
          count+=1
      if count > ans:
        ans = count
        index = i
    print(str(index) + " " + str(ans))
solve()