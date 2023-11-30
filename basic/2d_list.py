list_2=[[1,2,3],[4,5,6],[7,8,9]]
print(list_2[2][1])

list_2=[[1,2,3],[4,5,6],[7,8,9]]
print(len(list_2))
print(list_2[0])
print(list_2[2])

for i in range(5):
 for j in range(5):
  print(i,j)

list_2=[[1,2,3],[4,5,6],[7,8,9]]
num_of_rows=len(list_2)
for row in range(num_of_rows):
 col_size=len(list_2[row])
 for col in range(col_size):
  print(list_2[row][col])

for row in list_2:
 for col in row:
  print(col)

for row in list_2:
 print(row)























