class Employee:
  def __init__(self, id, importance, subordinates):
    # It's the unique id of each node.
    # unique id of this employee
    self.id = id
    # the importance value of this employee
    self.importance = importance
    # the id of direct subordinates
    self.subordinates = subordinates
class Solution:
  def getImportance(self, employees, id):
    a = []
    for i in range(len(employees)):
      a.append(Employee(employees[i][0], employees[i][1], employees[i][2]))

    x = a[0].id
    y = a[0].importance
    z = a[0].subordinates
    total = total(z)

Solution().getImportance([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1)

def total(n):
  total += n

if __name__ == '__main__':
  total = 0