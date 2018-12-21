# http://codeforces.com/problemset/problem/673/A?fbclid=IwAR0HbpiUxkRN7eTaeTKPVz_lfbABkFAM0eAvtDfaaWjTLhqXgy-rwpT0g38

interesting_minutes = int(raw_input())
minutes             = raw_input().split(' ')
count               = 0

for i in range(interesting_minutes):
  if ((int(minutes[i]) - count) > 15):
    count += 15
    break
  else:
    if (i == (interesting_minutes - 1) and int(minutes[i]) < 90):
      count = int(minutes[i]) + 15
    else:
      count = int(minutes[i])
if count > 90:
  print(90)
else:
  print(count)