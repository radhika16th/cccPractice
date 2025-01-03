# num = input()
# row = int(num[0])
# col = int(num[2])

# seq = []

# for i in range(row):
#     seq.append(input())

# for 

# for r in seq:
#     light = []
#     heavy = []

#     for i in range(col-2):
#         if r[i] != r[i+1] and r[i] == r[i+2]:
#             light.append('T') 
#         else:
#             heavy.append('F') 

#     print('T' if all(x == 'T' for x in light) else 'F')

# light = []
# heavy = []
# for r in seq:
#   for i in range(col):
#     if i % 2 == 0: 
#       light = [str(r[i]) if all()]

# that code does not work. come up with new logic where the code is simple and written in span of several lines, no functions are defined, no map() is used and only arrays are used. use the started code:


num = input()
T = int(num[0])
N = int(num[2])

seq = []

for i in range(T):
    seq.append(input())

for r in seq:
  alternating = ['T' if r[i] != r[i+1] and r[i] == r[i+2] else 'F' for i in range(N-2)]
  print(alternating)
  print('T' if all(x == 'T' for x in alternating) else 'F')
