# https://www.spoj.com/problems/STPAR/fbclid=IwAR0prTLXhHqrpt5dVh37JSqdppxt0VgYN6ttyspWYgx-cDQ3rBBO_HdGcfg
# STPAR - Street Parade

n      = int(raw_input())
cars   = map(int, raw_input().split(' '))
street = 1
stack  = []

for car in cars:
  while (len(stack) != 0 and stack[-1] == street):
    street += 1
    stack.pop()
  if car == street:
    street += 1
  else:
    stack.append(car)
  while (len(stack) != 0 and stack[-1] == street):
    street += 1
    stack.pop()

if street == n + 1:
  print('yes')
else:
  print('no')