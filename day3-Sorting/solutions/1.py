# https://codeforces.com/problemset/problem/169/A
# A. Chores

n, a, b = map(int, input().split())
h = list(map(int, input().split()))

h.sort()

print(h[b] - h[b - 1])