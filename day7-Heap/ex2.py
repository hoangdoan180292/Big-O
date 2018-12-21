import heapq

class PQEntry:
  def __init__(self, value):
    self.value = value
  def __lt__(self, other):
    return self.value > other.value

if __name__ == '__main__':
  n = int(input())
  a = raw_input().split(' ')
  h = []