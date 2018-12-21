# https://codeforces.com/problemset/problem/551/A
# A. GukiZ and Contest

class Student:
  def __init__(self, id, mark):
    self.id = id 
    self.mark = mark
     
    
n = int(input())
v = list(map(int, input().split()))
students = []
for i in range(0, n):
  temp = Student(i, v[i]) 
  students.append(temp)
students = sorted(students, key=lambda student: student.mark, reverse=True)

ranks = [0] * n

ranks[students[0].id] = 1 
for i in range(1, n):
  if (students[i].mark == students[i-1].mark): 
    ranks[students[i].id] = ranks[students[i-1].id]
  else:
    ranks[students[i].id] = i + 1
        
print(*ranks)