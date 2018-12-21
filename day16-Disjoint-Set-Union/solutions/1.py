# https://uva.onlinejudge.org/index.php?Itemid=8&option=com_onlinejudge&page=show_problem&problem=1549
# 10608 - Friends

def findSet(u):
  while u != parent[u]:
    u = parent[u]
  return u

def unionSet(u, v):
  up = findSet(u)
  vp = findSet(v)
  if vp != up:
    parent[vp] = up
    cnt[up] += cnt[vp]

if __name__ == '__main__':
  t = int(input())
  for cs in range(t):
    n, m = map(int, input().split())
    parent = [i for i in range(n)]
    cnt = [1 for i in range(n)]
    for i in range(m):
      u, v = map(int, input().split())
      unionSet(u-1, v-1)
    print(max(cnt))