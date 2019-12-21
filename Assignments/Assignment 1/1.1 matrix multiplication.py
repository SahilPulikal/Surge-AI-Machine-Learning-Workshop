# 1. Write a program to perform Matrix multiplication using python list only
# 2. Write a program to create an excel sheet with only one sheet in it. In this sheet write Cell number using Column names and row numbers, in each cell from A-Z Columns and 1-100 rows. For, e.g., Row 1 and COlumn A should have 'A1', Row 1 and COlumn B should have 'B1', etc. as content
# If anyone has any doubt or questions, you can reach at srahul07@gmail.com

X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[97,85,13,25],
    [64,73,34,34],
    [79,65,54,3]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]
for r in result:
   print(r)