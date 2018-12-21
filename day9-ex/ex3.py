# http://algote.com/team/problem_v1.php?id=211
# Soldier and Bananas

k, n, w = list(map(int, input().split()))
loan = 0

for i in range(w):
  price = (i + 1) * k
  if n < price:
    loan += price - n
    n = 0
  else:
    n = n - price
print(loan)