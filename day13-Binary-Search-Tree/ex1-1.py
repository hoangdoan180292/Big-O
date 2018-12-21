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

T = int(input())

for i in range(T):
  X, N = map(int, input().split())
  a = list(map(int, input().split()))
  s = createTree(a, X)

  if size(s) > N:
    print('Average')
  elif size(s) < N:
    print('Bad')
  elif size(s) == N:
    print('Good')