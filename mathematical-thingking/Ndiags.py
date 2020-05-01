mat = [[0,1,0],[0,1,0],[0,0,0]]
(i,j) = (1,1)

def check_conflict(mat,i,j):
    if(mat[i][j] == 1):
        if((mat[i-1][j] == 2) or (mat[i+1][j] == 2) or (mat[i][j-1] == 2) or (mat[i][j+1] == 2) or (mat[i+1][j-1] == 1) or (mat[i-1][j+1] == 1)):
            return True
    if(mat[i][j] == 2):
        if((mat[i-1][j] == 1) or (mat[i+1][j] == 1) or (mat[i][j-1] == 1) or (mat[i][j+1] == 1) or (mat[i-1][j-1] == 2) or (mat[i+1][j+1] == 2)):
            return True
    return False

check_conflict(mat, 1, 1)