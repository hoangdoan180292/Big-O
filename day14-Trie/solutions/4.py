# https://www.hackerrank.com/challenges/contacts/problem
# Contacts

class TrieNode:
  def __init__(self, c):
    self.count = c
    self.child = dict()
    self.child.clear()

def addContact(root, s):
  for c in list(s):
    if c in root.child:
      root = root.child[c]
    else:
      root.child[c] = TrieNode(0)
      root = root.child[c]
    root.count += 1
      
def countContacts(root, s):
  for c in list(s):
    if c in root.child:
      root = root.child[c]
    else:
      return 0
  return root.count

n = int(input())
root = TrieNode(0)
while (n > 0):
  n -= 1
  opt, arg = input().split()
  
  if opt[0] == 'a':
    addContact(root, arg)
  else:
    print(countContacts(root, arg))