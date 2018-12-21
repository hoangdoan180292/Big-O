# https://www.hackerrank.com/contests/womens-codesprint-2/challenges/minimum-loss
# Minimum Loss

class Node:
  def __init__(self, key = 0, left = None, right = None):
    self.key = key
    self.left = left
    self.right = right

  def find(self, x):
    if self.key == x:
      return self
    if self.right and self.key < x:
      return self.right.find(x)
    if self.left and self.key > x:
      return self.left.find(x)
    return None

  def insert(self, x):
    if x < self.key:
      if self.left:
        self.left.insert(x)
      else:
        self.left = Node(x)
    elif x > self.key:
      if self.right:
        self.right.insert(x)
      else:
        self.right = Node(x)

  def find_min(self):
    cur = self
    while cur.left:
      cur = cur.left
    return cur
  
  def remove(self, x):
    if x < self.key:
      self.left = self.left.remove(x)
    elif x > self.key:
      self.right = self.right.remove(x)
    else:
      if self.left == None:
        return self.right
      elif root.right == None:
        return self.left
      temp = self.right.find_min()
      self.key = temp.key
      self.right = self.right.remove(temp.key)
    return self

  def upper_bound(self, x):
    if self.key <= x:
      if self.right:
        return self.right.upper_bound(x)
      return None
    if self.left == None:
      return self
    tmp = self.left.upper_bound(x)
    if tmp != None:
      return tmp
    return self
    
class Set:
  def __init__(self):
    self.root = None
      
  def insert(self, x):
    if self.root:
      self.root.insert(x)
    else:
      self.root = Node(x)
          
  def remove(self, x):
    if self.root:
      self.root = self.root.remove(x)

  def find(self, x):
    if self.root:
      return self.root.find(x)
    return None

  def upper_bound(self, x):
    if self.root:
      return self.root.upper_bound(x)
    return None

def inp():
  return map(int, input().split(' '))

if __name__ == '__main__':
  n = int(input())
  a = list(inp())
  res = 1e5

  s = Set()
  for x in a:
    y = s.upper_bound(x)
    s.insert(x)
    if y == None:
        continue
    res = min(res, y.key - x)
  print(res)