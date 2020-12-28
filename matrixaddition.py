arr1 =[[1,2,3],[4,5,6],[7,8,9],[1,0,1]]

#arr2 = [[4,5,6],[3,4,5],[2,3,4],[1,2,3]]

arr2 = [[1,2,3],[4,5,6],[7,8,9],[1,0,1]]

add=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]


for i in range(0,4):
    for j in range(0,3):
        add[i][j] = arr1[i][j]+arr2[i][j]

print("matrix addition :")

for i in add:
    print(i)
