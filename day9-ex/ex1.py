import queue

queries = int(input())
results = []

for _ in range(queries):
  n, m = list(map(int, input().split()))
  priorities = list(map(int, input().split()))
  q = queue.Queue()
  count = 0
  works = [0]

  for i in range(n):
    works.append(i+1)
    q.put(i+1)
  k = works[m]

  if q.qsize() == 1:
    count += 1
  else:
    while q.qsize() > 1:
      priority      = priorities[0]
      next_priority = priorities[1]
      if priority < next_priority:
        q.put(q.get())
        priorities.pop(0)
        priorities.append(priority)
      else:
        if q.queue[0] == k:
          break
        else:
          count += 1
          q.get()
  results.append(count)

for result in results:
  print(result)