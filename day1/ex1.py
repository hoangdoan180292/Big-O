# http://codeforces.com/problemset/problem/691/A?fbclid=IwAR3MFYYG8ak4fZhV02QmMFyoUw4O4fkEBt0EJnk9k_rccOYCCoWSsiEM8Nk

buttons  = int(raw_input())
fastened = raw_input().split(' ')
count    = 0

if buttons == 1:
  if (int(fastened[0]) != 0):
    count += 1
else:
  for i in range(buttons):
    if (int(fastened[i]) == 0):
      count += 1
if count == 1:
  print('YES')
else:
  print('NO')