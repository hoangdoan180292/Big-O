class Solution:
  # @param A : tuple of integers
  # @return a list of integers
  def repeatedNumber(self, A):
    count = [0 for i in range(len(A) + 1)]
    for i in range(len(A)):
      count[A[i]] += 1
      
    for i in range(1, len(count)):
      if count[i] == 2:
        a = i
      if count[i] == 0:
        b = i
    return [a, b]
print(Solution().repeatedNumber([3, 1, 2, 5, 3]))