import queue

arr = []
results = []
if __name__ == '__main__':
  n = -1
  while n != 0:
    n = int(input())

    if n == 0:
      break

    arr.append(list(map(int, input().split())))
  for a in arr:
    pq = queue.PriorityQueue()

    count = 0
    cost = 0

    for x in a:
      pq.put(x)

    while count < (n - 1):
      tmp = pq.get()
      tmp += pq.get()
      pq.put(tmp)
      cost += tmp
      count += 1
      results.append(cost)
  for k in results:
    print(k)