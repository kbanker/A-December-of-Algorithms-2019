
num_rows = int(input('Enter the number of rows: '))
matrix = []

for i in range(num_rows):
  matrix.append(input().split(' '))

cheating_matrix = []

#print(matrix)
for r in range(len(matrix)):
  c_row = []
  row = matrix[r]
  for p in range(len(row)):
   person = row[p]
   c_num = 0
   if p > 0 and row[p-1] == person: c_num += 0.2
   if p + 1 < len(row) and row[p+1] == person: c_num += 0.2

   if p > 0 and r > 0 and matrix[(r-1)][p] == person: c_num += 0.3
   if r + 1 < len(matrix) and matrix[(r+1)][p] == person: c_num += 0.2

   if p > 0 and r > 0 and matrix[r-1][p-1] == person: c_num += 0.025
   if p > 0 and r + 1 < len(matrix) and matrix[(r+1)][p-1] == person: c_num += 0.025

   if r > 0 and p + 1 < len(matrix[r-1]) and matrix[r-1][p+1] == person: c_num += 0.025
   if r + 1 < len(matrix) and p + 1 < len(row) and matrix[r+1][p+1] == person: c_num += 0.025

   c_row.append(c_num)

  cheating_matrix.append(c_row)

for row in cheating_matrix:
    print(row)
