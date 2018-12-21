# http://lightoj.com/volume_showproblem.php?problem=1224
# 1224 - DNA Prefix

def inp():
  return map(int, input().split())

class TrieNode:
  def __init__(self):
    self.child = dict()
    self.child.clear()
    self.value = 0
    self.flag = False

def addString(root, s):
  for c in list(s):
    if c in root.child:
      root = root.child[c]
    else:
      root.child[c] = TrieNode()
      root = root.child[c]
    root.value += 1

def get(root, s):
  value_max = 0
  len = 0
  for c in list(s):
    if c in root.child:
      root = root.child[c]
    len+=1
    value_max = max(value_max, root.value * len)
  return value_max

def clear(root):
  if root is None:
    return
  for c in root.child:
    clear(root.child[c])
  del root
  root = None

def solve() :
  testcase = int(input())
  for t in range(testcase):
    ans = 0
    n = int(input())
    a = []
    for i in range(n):
      a.append(input())
    root = TrieNode()
    for i in range(n):
      addString(root, a[i])
    for i in range(n):
      ans = max(ans, get(root, a[i]))
    print("Case {}: {}".format(t + 1, ans))
    clear(root)
solve()