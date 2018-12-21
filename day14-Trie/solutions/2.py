# https://www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/practice-problems/algorithm/search-engine/ 
# Search Engine

def inp():
    return map(int, input().split())

class TrieNode:
  def __init__(self, c):
    self.c = c
    self.child = dict()
    self.child.clear()
    self.value = -1
    self.flag = False


def addString(root, s, value):
  for c in list(s):
    if c in root.child:
      root = root.child[c]
    else:
      root.child[c] = TrieNode(c)
      root = root.child[c]
    if root.flag:
      return False
  root.flag = True
  root.value = value
  return True

def get(root, s):
  for c in list(s):
    if c in root.child:
      root = root.child[c]
    else:
      return -1
  return root.value

def DFS_Trie(root):
  for c in root.child:
    DFS_Trie(root.child[c])
    root.value = max(root.value, root.child[c].value)

def solve() :
  n, m = inp()
  root = TrieNode('$')
  for i in range(n):
    line = input().split()
    addString(root, line[0], int(line[1]))
  DFS_Trie(root)
  for i in range(m):
    line = input()
    print(get(root, line))
solve()