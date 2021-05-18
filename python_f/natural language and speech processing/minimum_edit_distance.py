a#Daniel Gallab
#CPSC475: project 5
#minimum edit distance
#uses dynamic programming to measure word similarity



def create_table(w1,w2):
    mat=['-']*(len(w1)+1)
    for i in range(len(mat)):
        mat[i]= [0]*(len(w2)+1)
    for x in range(1,len(mat)):
        mat[x][0] = x
    for y in range(1,len(mat[0])):
        mat[0][y]= y
    print(mat)
    return (mat)


def min_edit_dist(mat,w1,w2):
    mat_b=create_table(w1,w2)
    
    for x in range(1,len(mat)):
        for y in range(1,len(mat[0])):
            ptr=[]
            mat[x][y]= min(mat[x-1][y]+1, mat[x][y-1]+1, mat[x-1][y-1]+sub_cost(w1[x-1],w2[y-1]))
            if (mat[x][y] == (mat[x-1][y-1])+sub_cost(w1[x-1],w2[y-1])):
                ptr=ptr+["s"] # diagonal pointer
            if x==0 or(mat[x][y] == (mat[x-1][y])+1):
                ptr=ptr+["i"] # up pointer
            if y==0 or (mat[x][y] == (mat[x][y-1])+1):
                ptr=ptr+["d"] #left pointer 
            mat_b[x][y] = ptr
    
            

    mat_b[0] = len(mat_b[0])*[["d"]]
    for i in range(len(mat_b)):
        mat_b[i][0] = ["i"]
    mat_b[0][0] = 0

    for i in range(len(mat)):
        print (mat[i])
            
    print("\n")
    
    for i in range(len(mat_b)):
        print (mat_b[i])

    
    
    return (mat[len(mat)-1][len(mat[0])-1],mat,mat_b)

def back_trace(mat_b):
    
    x=len(mat_b)-1
    y=len(mat_b[0])-1
    #start at right bottom corner

    while (mat_b[x][y] != 0):
        if "s" in mat_b[x][y]:
            x=x-1
            y=y-1
            print("s")
        elif "i" in mat_b[x][y]:
            x=x-1
            print("i")
        elif "d" in mat_b[x][y]:
            y=y-1
            print("d")
        
    
    
        
def sub_cost(char1, char2):
    if char1==char2:
        return 0
    else:
        return 2
    
def main():
   # w2 =/
   # w1 =/
    source = input("Enter source word")
    target = input("Enter target word")
    mat = create_table(source,target)
    d,mat,mat_b = min_edit_dist(mat,source,target)
    print("minimum edit distance: ", d)
    back_trace(mat_b)

main()
