col = int(input())

row1 = [int(n) for n in input().split()]
row2 = [int(n) for n in input().split()]

a = []

# for i in range(col):
#   if row1[i] == row2[i]:
#     a.append("Y")

# if (len(a) == col):
#   print("YES")
# else:
#   print("NO")


def transform_array(A, B):
  operations = []
  
  for i in range(len(A)):
    diff = B[i] - A[i]
    if diff != 0:
        if diff > 0:
            operation = "R {} {}".format(i, i + diff - 1)
        else:
            operation = "L {} {}".format(i - diff, i - 1)
        operations.append(operation)
        for j in range(i, i + diff, diff // abs(diff)):
            A[j] = A[i]
  
  return A == B, operations

# Input reading
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

possible, operations = transform_array(A, B)

if possible:
    print("YES")
    print(len(operations))
    for operation in operations:
        print(operation)
else:
    print("NO")
