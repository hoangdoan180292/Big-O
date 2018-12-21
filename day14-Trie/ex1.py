class Node:
  def __init__(self):
    self.countWord = 0
    self.maxPriority = 0
    self.child = dict()

def addWord(root, s, priority):
  tmp = root
  for ch in s:
    if ch not in tmp.child:
      tmp.child[ch] = Node()
    tmp = tmp.child[ch]
    tmp.maxPriority = max(tmp.maxPriority, priority)
  tmp.countWord += 1

def findWord(root, s):
  tmp = root
  for ch in s:
    if ch not in tmp.child:
      return 0
    tmp = tmp.child[ch]
  return tmp.maxPriority

if __name__ == '__main__':
  n, q = list(map(int, input().split()))

  root = Node()

  for i in range(n):
    word, weight = list(input().split())
    addWord(root, word, int(weight))
  for i in range(q):
    k = input()
    result = findWord(root, k)

    if result == 0:
      print(-1)
    else:
      print(result)