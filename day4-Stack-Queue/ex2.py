# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1876&fbclid=IwAR0pXJACwdgmWHCO6U5H2-hisNaVmhAdbn6AIkyNW4zTw2ZHO31vrgRCmUw
# 10935 - Throwing cards away I

import queue
n = int(input())
arr = []
q = queue.Queue()

while n != 0:
  arr.append(n)
  n = int(input())

for x in range(len(arr)):
  discarded_cards = []
  number = arr[x]

  if number < 1:
    break

  if number == 1:
    print("Discarded cards:")
    print("Remaining card: %d" % 1)
  else:
    for i in range(number):
      q.put(i + 1)

    while q.qsize() > 1:
      discarded_cards.append(q.get())
      q.put(q.get())

    print("Discarded cards:", ', '.join(map(str, discarded_cards)))
    print("Remaining card: %d" % q.get())