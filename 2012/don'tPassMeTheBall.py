J = int(input())
count = 0

for i in range(1, J):
  for j in range(i+1, J):
    for k in range(j+1, J):
        count += 1

print(count)
