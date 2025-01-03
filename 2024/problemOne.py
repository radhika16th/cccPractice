N = int(input())
seat = []
oppo_seat = []

for i in range(N//2):
  seat.append(int(input()))

for i in range(N//2):
  oppo_seat.append(int(input()))

count = 0

for i in range(N//2):
  if seat[i] == oppo_seat[i]:
    count += 2

print(count)
