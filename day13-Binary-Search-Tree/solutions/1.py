# https://www.hackerearth.com/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/distinct-count/
# Distinct Count

class Node:
  def __init__(self, key = 0, left = 0, right = 0):
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
  
  def size(self):
    size_left = 0
    size_right = 0
    if self.left:
      size_left = self.left.size()
    if self.right:
      size_right = self.right.size()
    return size_left + size_right + 1
    
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
  
  def size(self):
    if self.root:
      return self.root.size()
    return 0

if __name__ == '__main__':
  t = int(input())
  print(t)
  for cs in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    s = Set()
    for e in a:
      s.insert(e)
    sz = s.size()
    if sz == x:
      print("Good")
    elif sz < x:
      print("Bad")
    else:
      print("Average")