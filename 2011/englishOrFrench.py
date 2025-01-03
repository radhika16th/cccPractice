N = int(input())
countT = 0
countS = 0

for i in range(N):
  line = input()

  for letter in line:
    if ((letter == 's') or (letter == 'S')):
      countS += 1
    if ((letter == 't') or (letter == 'T')):
      countT += 1

if countT > countS:
  print("English")
else:
  print("French")
