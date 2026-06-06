ARR = [[1,2,3,4],[2,3,4,5],[6,7,8,9]]
rows = len(ARR)
clm = len(ARR[0])
for i in range (0,rows):
    for j in range (0,clm):
        print(ARR[i][j],end = " ")
print()


#PRINT THE UPPER DIAGONAL
num = [[1,2,3,4],[2,3,4,5],[6,7,8,9]]
rows = len(num)
clm = len(num[0])
for i in range (0,rows):
    for j in range(0,clm):
        if j>= i:
            print(num[i][j],end = " ")
        else:
            print("*",end=" ")
print()

#traverse the matrix in spiral form
spiral = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
"""before that create a matrix to store which has 0 and you replace with the matrix element when you visit it, so that you can keep track of which element is visited and which is not visited, and also create a list to store the result of the spiral traversal"""
rows = len(spiral)
clm = len(spiral[0])
result  = [[0]*rows for _ in range(clm)] #this is imp it will create a 4 rows and and 4 column
for i in range (0,rows):
    for j in range (0,clm):
        result[i][j] = spiral[i][j]
print(result)

#SET MATRIX ZERO
#BRUTE FORCE SOLUTION
def mark_infinity(matrix,row,col):
    rows = len(matrix)
    clm = len(matrix[0])
    for i in range (0,rows):
        if matrix[i][col] != 0:
            matrix[i][col] = float('inf')
    for j in range(0,clm):
        if matrix[row][j] != 0:
            matrix[row][j] = float('inf')

def set_matrix_zero(matrix):
    r = len(matrix)
    c = len(matrix[0])
    for i in range (0,r):
        for j in range (0,c):
            if matrix[i][j] == 0:
                mark_infinity(matrix,i,j)
    for i in range (0,r):
        for j in range (0,c):
            if matrix[i][j] == float('inf'):
                matrix[i][j] = 0


#driver code
matrix = [[1,2,3],[4,0,6],[7,8,9]]
set_matrix_zero(matrix)
print(matrix)   