# http://codeforces.com/problemset/problem/731/A?fbclid=IwAR2Sm0sVALCT3aDpmqCOykIlGtOHRYsukrac-GAKtkLuzeePm0pL88XwRN0

text    = str(input())
pointer = 'a'
count   = 0

for i in range(len(text)):
  dist = abs(ord(pointer) - ord(text[i]))
  if (dist < 13):
    count += dist
  else:
    count += (26 - dist)
  pointer = text[i]

print(count)