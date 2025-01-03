line = str(input())
unit = []
unit = line.split()

line2 = str(input())
patients = []
patients = line2.split()

blood = ["O negative", "O positive", "A negative", "A positive", "B negative", "B positive", "AB negative", "AB positive"]

count = 0

for i in range(8):
  if (int(unit[i]) > 0 and int(patients[i]) > 0):
    if (int(unit[i]) >= int(patients[i])):
      count += int(patients[i])
    else:
      count += int(unit[i])

print(count)
