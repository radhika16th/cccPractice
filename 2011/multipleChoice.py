num = int(input())

count = 0

answers = []
correct = []

for i in range(num):
  a = input()
  answers.append(a)

for i in range(num):
  b = input()
  correct.append(b)

for i in range(num):
  if answers[i] == correct[i]:
    count += 1

print(count)
