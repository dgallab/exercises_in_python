import math


def create_adj_table(): #N stores the node paths.
  inf = math.inf
  header=['*','u','v','x','y','z']
  u=['u',0,1,inf,2,inf]
  v=['v',1,0,3,inf,6]
  x=['x',inf,3,0,3,2]
  y=['y',2,inf,3,0,inf]
  z=['z',inf,6,2,inf,0]
  N=[header, u,v,x,y,z]
  return (N)



def path_weight(startnode,endnode,N):
   # print ("I am here",startnode)
    #print ("I am there",endnode)
    for i in range(1,len(N)):
        if N[0][i] == startnode:
            x=i
        if N[0][i]== endnode:
            y=i
    return N[y][x]

def modify_table(ST,source,target,new_dis):
    i=0
    for e in ST[0]:
        print(e)
        if e == source:
            x=i
        if e == target:
            y=i
        i = i + 1
    ST[x][y] = new_dis
    return(ST)

def get_closest_node(source,Q,N):
    min_index=-1
    minimum=math.inf
    for i in range(0,len(N)):
        if N[0][i] == source:
            x=i
   
    for j in range(1,len(N[x])):
        if N[x][j] <= minimum and N[j][0] in Q:
            minimum = N[x][j]
            y=j
    return (N[y][0])
    

        
    

def dijkstras(N,source):
    inf = math.inf
    Q={'u','v','x','y','z'}
    dis = {'u': inf,'v': inf,'x': inf,'y':inf,'z':inf}
    prev = {'u': None,'v':None,'x':None,'y':None,'z':None}
    dis[source] = 0
    
    while len(Q) > 0:
        cn = get_closest_node(source,Q,N)
        Q=Q-{cn}
        
        for v in Q:
            alt = dis[cn] + path_weight(cn,v,N)
            if alt < dis[v]:
                dis[v]=alt
                prev[v] = cn
    print(dis)
    print(prev)
    return (dis,prev)
                    
        
        
    
  
def main():
    N=create_adj_table()
    #print(modify_table(ST,'z','v',2))
    
    dijkstras(N,'u')




main()
