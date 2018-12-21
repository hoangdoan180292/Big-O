# http://lightoj.com/volume_showproblem.php?problem=1129
# 1129 - Consistency Checker

class Node:
  countLeaf = 0
  child = dict()
  def __init__(self):
    self.countLeaf = 0
    self.child = dict()

def addWord(root, s):
  tmp = root
  flag = False
  for ch in s:
    if ch in tmp.child:
      tmp = tmp.child[ch]
    else:
      tmp.child[ch] = Node()
      tmp = tmp.child[ch]
      flag = True
    if tmp.countLeaf > 0:
      flag = False
      break
  tmp.countLeaf += 1
  return flag

def clear(root):
  if root is None:
    return
  for child in root.child.values():
    clear(child)
  del root

def solve() :
  testcase = int(input())
  for t in range(testcase):
    n = int(input())
    ans = True

    root = Node()
    for i in range(n):
      line = input()
      ans = ans & addWord(root, line)
    if ans:
      print("Case " + str(t + 1) + ": YES")
    else:
      print("Case " + str(t + 1) + ": NO")
    clear(root)

solve()