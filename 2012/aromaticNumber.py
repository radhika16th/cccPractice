num = str(input())

symbol = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
base = [1, 5, 10, 50, 100, 500, 1000]

sum = 0
p_base = 0

for i in range(0, len(num), 2):
  for j in range(len(symbol)):
    if num[i+1] == symbol[j]:
      if p_base < base[j] and p_base != 0:
        sum -= int(num[i]) * base[j]
      else:
        sum += int(num[i]) * base[j]
      p_base = base[j]

print(sum)
