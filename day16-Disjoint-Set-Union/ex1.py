# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1549
# 10608 - Friends

def makeSet():
  global parent, count
  parent = [i for i in range(n+1)]
  count = [1 for i in range(n+1)]

def findSet(u):
  if parent[u] != u:
    parent[u] = findSet(parent[u])
  return parent[u]

def unionSet(u, v):
  up = findSet(u)
  vp = findSet(v)
  if up != vp:
    parent[vp] = up
    count[up] += count[vp]
  # if up == vp:
  #   return
  # if ranks[up] > ranks[vp]:
  #   parent[vp] = up
  # elif ranks[up] < ranks[vp]:
  #   parent[up] = vp
  # else:
  #   parent[up] = vp
  #   ranks[vp] += 1

if __name__ == '__main__':
  q = int(input())
  for i in range(q):
    n, m = list(map(int, input().split()))
    makeSet()
    for i in range(m):
      u, v = list(map(int, input().split()))
      unionSet(u, v)
    print(max(count))