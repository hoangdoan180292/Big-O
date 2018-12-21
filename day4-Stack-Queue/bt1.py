# https://www.spoj.com/problems/ONP/
# ONP - Transform the Expression


# Y tưởng:
  # - Tạo 1 array chứa những chuỗi nhập vào
  # - Lặp từng phần tử của array vừa có được
  # - Lặp từng ký tự của string:
  #   + Nếu không phải là toán tử: đưa vào kết quả
  #   + Nếu là toán tử:
  #     + Nếu gặp phần tử là ')' thì lấy tất cả toán tử trên cùng của stack đến khi gặp dấu '('

def getPriority(op):
  if op == "*" or op == "/" or op == "%":
    return 2
  elif op == "+" or op == "-":
    return 1
  else:
    return 3

def isOperand(op):
  if (48 <= ord(op) and ord(op) <= 57) or (65 <= ord(op) and ord(op) <= 90) or (97 <= ord(op) and ord(op) <= 122):
    return 0
  else:
    return 1

n       = int(input())
strings = []
stack   = []

if n < 1:
  exit()

for i in range(n):
  strings.append(input())
  
for string in strings:
  characters = list(string)
  result = []
  for x in characters:
    if isOperand(x) == 1:
      if x != '(' and x != ')' and getPriority(stack[-1]) < getPriority(x):
        result.append(stack[-1])
      else:
        if x == ')':
          while len(stack) > 0 and stack[-1] != '(':
            result.append(stack.pop())
            if len(stack) > 0 and stack[-1] == '(':
              stack.pop()
        else:
          stack.append(x)
    else:
      result.append(x)
  print(''.join(result))