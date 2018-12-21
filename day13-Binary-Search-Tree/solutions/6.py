# https://codeforces.com/problemset/problem/424/B
# B. Megacity

import math

def solve():
  numLocation, totalPeople = map(int, input().split())
  location = dict()
  for i in range(numLocation):
    x, y, people = map(int, input().split())
    r = x * x + y * y
    if r in location:
      location[r] += people
    else:
      location[r] = people
  radius = []
  for r in location:
    radius.append(r)
  radius.sort()
  for r in radius:
    totalPeople += location[r]
    if totalPeople >= 1000000:
      print(math.sqrt(r))
      return
  print("-1")
    
solve()