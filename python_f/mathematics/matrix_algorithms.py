

def create_matrix(r,c):
    mat = r*[0]
    for i in range(0,len(mat)):
       mat[i] = c *[0]
    return mat

def add_matrices(matA,matB):
     new_mat = create_matrix(len(matA),len(matA[0]))
     for i in range(0,len(new_mat)):
        for j in range(0,len(new_mat[0])):
            new_mat[i][j] = matA[i][j]+ matB[i][j]
     for e in new_mat:
         print(e)
     print("")
     return new_mat
    

def multiply_matrices(matA,matB):
    assert len(matB) == len(matA[0])
    new_mat = create_matrix(len(matA),len(matB[0]))

    for i in range(0,len(new_mat)):
        for j in range(0,len(new_mat[0])):
            new_mat[i][j] = dot_product(matA[i], linearize(matB,j))
            
    for e in new_mat:
        print (e)
    print("")
    return new_mat

def calc_determinant(matX):
    if len(matX)==1:
        return matX[0][0]
    else:
        lst = []
        for i in range(0,len(matX)):
             lst.append(matX[0][i]*(-1)**i*calc_determinant(mask(matX,0,i)))
        return sum(lst)


    
def mask(matX,r,c):
    new_matrix=create_matrix(len(matX)-1,len(matX)-1)
    e = 0
    f = 0
    for i in range(0,len(matX)):
        for j in range(0,len(matX)):
            if not(i==r or j==c):
                new_matrix[e][f] = matX[i][j]
                if e == len(new_matrix)-1 and f == len(new_matrix)-1:
                    e=e
                    f=f
                elif f == len(new_matrix)-1:
                    f=0
                    e=e+1
                else:
                    f=f+1
    return new_matrix


    
        
        #return calc_determinant_loop(mat_lst)

                
def linearize(matB,j):
    lstB = []
    for v in range(0,len(matB)):
        lstB=lstB + [matB[v][j]]
    return lstB
    
def dot_product(lstA,lstB):
    assert len(lstA) == len(lstB)
    dp = 0
    for i in range(0,len(lstA)):
        dp=dp+lstA[i]*lstB[i]
    return dp

def fill_matrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
          mat[i][j] = i * j - 2
    for e in mat:
        print (e)
    print("")
    return mat


def display(mat):
    for e in mat:
        print (e)
    
def main():
    matA = create_matrix(6,3)
    matB = create_matrix(3,8)
    matA = fill_matrix(matA)
    matB = fill_matrix(matB)
    matC=multiply_matrices(matA,matB)
    #matC = create_matrix(4,4)
    #matD = create_matrix(4,4)
    #add_matrices(matC,matD)
    matX=[[1,2,3],
          [9,20,6],
          [7,8,9]]

    matY=[[1,2],
          [3,4]]

    matV=[[7,2,-6,-5],
          [1,3,-2,0],
          [4,10,-9,7],
          [1,7,-12,3]]
    
    matZ=[[1]]
    
    #print(mask(matX,0,2))
    #mask_loop(matX)
    print(calc_determinant(matV))
main()
