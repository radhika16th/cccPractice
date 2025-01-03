C = int(input())

row1 = [int(n) for n in input().split(' ')]
row2 = [int(n) for n in input().split(' ')]

count = 0

for i in range(C):
  if row1[i] == 1:
    count += 3
    print(count)
    if i != C-1:
      if row1[i+1] == 1:
        count -= 1
        print(count)
      if row1[i-1] == 1:
        count -= 1
        print(row1[i-1],count)
      if row2[i] == 1:
        count -= 1
        print("2", count)
  print()
  if row2[i] == 1:
    count += 3
    print(count)
    if i != C-1:
      if row2[i+1] == 1:
        count -= 1
        print(count)
      if row2[i-1] == 1:
        count -= 1
        print(count)
      if row1[i] == 1:
        count -= 1
        print(count)
  print()

print(count)
