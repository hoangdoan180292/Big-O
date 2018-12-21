# https://www.spoj.com/problems/ONP/
# ONP - Transform the Expression

t = int(input()) 

while(t>0):
  Expression = input()
  s = []
  for e in Expression: 
    if e.islower():
      print(e, end = '')
    elif e == ")":
      print(s[-1],end = '')
      s.pop()
    elif e != "(":
      s.append(e)
  t -= 1
  print()