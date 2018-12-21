n = int(input())

if n % 2 == 0:
  exit()
  
a = list(map(int, input().split()))
sorted = sorted(a)
b = len(sorted)/2
print(sorted[int(b)])