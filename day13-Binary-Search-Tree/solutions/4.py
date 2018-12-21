# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1167
# 10226 - Hardwood Species

import sys

class Node:
  def __init__(self, key = 0, value = 0, left = None, right = None):
    self.key = key
    self.value = value
    self.left = left
    self.right = right
 
  def insert(self, x):
    if x < self.key:
      if self.left:
        return self.left.insert(x)
      else:
        self.left = Node(x)
        return self.left
    elif x > self.key:
      if self.right:
        return self.right.insert(x)
      else:
        self.right = Node(x)
        return self.right
    return self
    
class Set:
  def __init__(self):
    self.root = None
      
  def insert(self, x):
    if self.root:
      return self.root.insert(x)
    else:
      self.root = Node(x)
      return self.root

def print_trees(root, total):
  if root:
    print_trees(root.left, total)
    print('%s %.4f' % (root.key, 100 * root.value / total))
    print_trees(root.right, total)

T = int(input())
try:
  input()
  for tc in range(T):
    species = Set()
    total = 0
    while True:
      specie = input()
      if specie == '':
          break
      total += 1
      cur = species.insert(specie)
      cur.value += 1
    print_trees(species.root, total)
    if tc < T - 1:
      print()
except EOFError:
  print_trees(species.root, total)
  sys.exit(0)