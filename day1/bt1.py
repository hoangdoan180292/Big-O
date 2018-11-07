# http://codeforces.com/problemset/problem/242/B 

number_segments = int(raw_input())
segments = []

for i in range(number_segments):
  segments.append(raw_input().split(' '))

for i in range(len(segments)):
  if i == (number_segments - 1):
    break
  else:
    current_segment = segments[i]
    next_segment = segments[i+1]
    
    if ge(int(next_segment[0]), int(current_segment[0])) and le(int(next_segment[-1]), int(current_segment[-1])):
      print('OK')