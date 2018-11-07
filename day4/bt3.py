# https://www.spoj.com/problems/MMASS
# ((CH)2(OH2H)(C(H))O)3

# Ý tưởng:
# Tạo 1 stack
# Lặp từng ký tự của chuỗi nhập vào:
#   + Nếu là '(', thêm -1 vào stack
#   + Nếu là 'H, C, O', thêm giá trị tương ứng vào stack
#   + Nếu là ')', tính tổng giá trị của các phần tử đầu stack (đến đâu remove đến đó) đến khi nào gặp -1 thì thay tổng giá trị tính được vào vị trí của -1 đó.

def convertStrToNumber(string):
  if string == 'H':
    return 1
  elif string == 'C':
    return 12
  elif string == 'O':
    return 16
  else:
    return 0

characters = list(input())
stack = []

for character in characters:
  if character == '(':
    stack.append(-1)
  elif character == ')':
    x = 0
    while stack[-1] != -1:
      x += stack.pop()
    stack.pop() # remove -1
    stack.append(x)
  elif character.isdigit():
    stack.append(stack.pop()*int(character))
  else:
    stack.append(convertStrToNumber(character))

print(sum(stack))