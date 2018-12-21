# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3359
# 12207 - That is Your Queue

# Input:
# 3 6
# N
# N
# E 1
# N
# N
# N
# 10 2
# N
# N
# 0 0

# Sample Output
# Case 1:
# 1
# 2
# 1
# 3
# 2
# Case 2:
# 1
# 2

# Y tưởng:
# B1: Đọc dữ liệu
#   - Khai báo mảng chứa dãy số nhập vào [], nếu phần tử đầu tiên nhập vào là số:
#     + Nếu mảng đó rỗng thì đưa dữ liệu vừa nhập vào
#     + Ngược lại đưa mảng đó vào 1 mảng chứa các dãy số lần chúng ta cần làm, sau đó reset mảng con, thêm phần tử vừa nhập vào

# B2: Lọc từng phần tử của những dãy cần làm
#   - Mảng results chứa các số thứ tự cần in ra
#   - Lọc từng phần tử của 1 dãy(arr):
#      + Nếu là 'N' thì xóa phần tử đầu tiên, đưa phần tử đó vào mảng results, sau đó thêm phần tử đó vào cuối mảng chứa các phẩn tử của dãy đó (arr)
#      + Ngược lại xóa phần tử được ưu tiên trong mảng chứa các phần tử của dãy (arr), sau đó chèn phần tử đó lên đầu mảng chứa các phần tử của dãy (arr)

def print_result(results):
  for a in results:
    print(a)

arr_input = [] # Chứa dãy cần xử lý
n = ['-1']
x = [] # Chứa số lượng phần tử của 1 dãy

while n[0] != '0':
  n = input()
  if n[0] != '0':
    if n[0].isdigit():
      if len(x) > 0:
        arr_input.append(x)
        x = [n]
      else:
        x = [n]
    else:
      x.append(n)
arr_input.append(x)

for i in range(len(arr_input)):
  results = []
  arr = []
  numbers = list(map(int, arr_input[i].pop(0).split())) # VD: 3 6 thì sẽ lấy phần tử nhỏ hơn là 3
  for j in range(min(numbers)): # tao mang gom number phan tu
    arr.append(j+1)
  for step in arr_input[i]:
    if step == 'N':
      value = arr.pop(0)
      results.append(value) # Thêm vào kết quả
      arr.append(value) # Đưa vào cuối mảng
    else:
      # E 1
      emergencies = step.split()
      try:
        arr.remove(int(emergencies[-1]))
      except Exception as e:
        pass
      arr.insert(0, int(emergencies[-1]))
  print("Case %d:" % int(i+1))
  print_result(results)