# http://acm.timus.ru/problem.aspx?num=1585
# 1585. Penguins

def solve():
  n = int(input())
  S = dict()
  for i in range(n):
    name = input()
    if name in S:
      S[name] = S[name] + 1
    else:
      S[name] = 1
  ans = ""
  max = 0
  for item in S:
    if S[item] > max:
      max = S[item]
      ans = item
  print (ans)

solve()