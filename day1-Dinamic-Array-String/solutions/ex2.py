# https://codeforces.com/problemset/problem/731/A
# A. Night at the Museum

wheel = input()
ch = 'a'
count = 0
m = 0
for i in wheel:
  m = abs(ord(ch) - ord(i))
  if (m < 13):
    count = count + m
  else:
    count = count + 26 - m
  ch = i
print("%d" % (count));