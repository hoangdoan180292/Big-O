# https://uva.onlinejudge.org/index.php?Itemid=8&option=com_onlinejudge&page=show_problem&problem=2498
# 11503 - Virtual Friends

import sys
import threading
class Scanner:
  def __generator__():
    while True:
      for x in input().strip().split():
        yield x
  sc = __generator__()
  def next():
    return Scanner.sc.__next__()
Sc = Scanner

def getroot(lab, u):
  while lab[u] != -1:
    u = lab[u]
  return u

def union(lab, cou, a, b):
  if cou[a] > cou[b]:
    cou[a] += cou[b]
    lab[b] = a
  else:
    cou[b] += cou[a]
    lab[a] = b

def solve():
  testcase = int(Sc.next())
  for t in range(testcase):
    n = int(Sc.next())
    people = dict()
    cnt = 0
    lab = []
    cou = []
    for i in range(n):
      people1, people2 = Sc.next(), Sc.next()
      if people1 in people:
        u = people[people1]
      else:
        u = cnt
        people[people1] = cnt
        lab.append(-1)
        cou.append(1)
        cnt+= 1
      if people2 in people:
        v = people[people2]
      else:
        v = cnt
        people[people2] = cnt
        lab.append(-1)
        cou.append(1)
        cnt+= 1
      u = getroot(lab, u)
      v = getroot(lab, v)
      if (u == v):
        print(cou[u])
      else:
        print(cou[u] + cou[v])
        union(lab, cou, u, v)

solve()