n = int(input())
a = list(input().lower())
count = 0
alphabet = list('abcdefghijklmnopqrstuvwxyz')

for x in alphabet:
  if x in a:
   count += 1

if count < 26:
  print('NO')
else:
  print('YES')