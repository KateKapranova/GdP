#algorithm to calculate the matrix of a complement graph
def complementMatrix(m):

    #initialising the matrix of the complement graph
    rows = len(m)
    columns = len(m[0])
    comp = [[0 for i in range(columns)] for i in range(rows)]

    #calculate the complement matrix:
    for i in range(rows):
        for j in range(columns):
            comp[i][j]= 1-m[i][j]

    return comp

#test cases
A=[[0,0,1],[0,1,0],[1,0,0]]
B=[[1,1,0,0],[1,0,0,1],[0,0,0,0],[0,1,0,0]]
print("matrix A=",A)
print("matrix B=",B)
print("Complement graph of matrix A:", complementMatrix(A))
print("Complement graph of matrix B:", complementMatrix(B))
