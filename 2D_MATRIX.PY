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
            