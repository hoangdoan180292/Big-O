# https://www.spoj.com/problems/MMASS/
# MMASS - Mass of Molecule

s = input().strip() # test input có khoảng trắng
stack = []
mass = {'H': 1, 'C': 12, 'O': 16}

for c in s:
  if c.isalpha():
    stack.append(mass[c])
  elif c.isnumeric():
    top = stack[-1]
    stack.pop()
    stack.append(top * int(c))
  elif c == '(':
    stack.append(c)
  elif c == ')':
    w = 0
    while stack[-1] != '(':
      w += stack[-1]
      stack.pop()
    stack.pop()
    stack.append(w)
print(sum(stack))