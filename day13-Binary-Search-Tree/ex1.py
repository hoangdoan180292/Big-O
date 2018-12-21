# https://www.hackerearth.com/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/distinct-count/description/?fbclid=IwAR2okMchIhyAhQV3Zxlga-xkK7XMLowjky1GsLfhfyUQT89eGDYY-aRv8zo
# Distinct Count

T = int(input())

for i in range(T):
  X, N = map(int, input().split())
  a = list(map(int, input().split()))
  s = set(a)

  if len(s) > N:
    print('Average')
  elif len(s) < N:
    print('Bad')
  else:
    print('Good')