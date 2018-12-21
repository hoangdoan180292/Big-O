class Node:
  def __init__(self):
    self.key = 0
    self.left = None
    self.right = None

def createNode(x):
  newNode = Node()
  newNode.key = x
  return newNode

def insertNode(root, x):
  if root == None:
    return createNode(x)
  if x < root.key:
    root.left = insertNode(root.left, x)
  elif x > root.key:
    root.right = insertNode(root.right, x)
  return root

def createTree(a, n):
  root = None
  for i in range(n):
    root = insertNode(root, a[i])
  return root

def size(root):
  if root == None:
    return 0
  return size(root.left) + 1 + size(root.right)

def searchNode(root, x):
  if root == None or root.key == x:
    return root
  if root.key < x:
    return searchNode(root.right, x)
  return searchNode(root.left, x)

T = int(input())
such_a = []
such_b = []

for i in range(T):
  N, M = map(int, input().split())
  a = list(map(int, input().split()))
  for i in range(N):
    such_a.append(a[i])
  s = createTree(such_a, N)

  for i in range(M):
    k = a[i + N]

    if size(searchNode(s, k)) > 0:
      print('YES')
    else:
      print('NO')
      insertNode(s, k)