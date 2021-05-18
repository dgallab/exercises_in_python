#Bellman Ford algorithm

import math


def create_adj_table(): #N stores the node paths.
#However the data for the source distance is stored in a different array 
  inf = math.inf
  header=['*','u','v','x','y','z']
  u=['u',0,1,inf,2,inf]
  v=['v',1,0,3,inf,6]
  x=['x',inf,3,0,3,2]
  y=['y',2,inf,3,0,inf]
  z=['z',inf,6,2,inf,0]
  N=[header, u,v,x,y,z]
  return (N)

#given 2 nodes, look up the distance between them in an adjacency table
def path_weight(startnode,endnode,N):
    for i in range(1,len(N)):
        if N[0][i] == startnode:
            x=i
        if N[0][i]== endnode:
            y=i
    return N[y][x]

    
def Bellman_Ford(source,N):
  inf = math.inf
  vertices = N[0][1:len(N)]
  distances=[inf] * (len(N)-1)
  predecessors = [None] *(len(N)-1)
  #find position of source in array and define the corresponding position in the
  #distance array to be 0. the rest of the values are inf
  for i in range(0,len(vertices)):
      if vertices[i] == source:
          distances[i] = 0
  
  for i in range(1,len(vertices)-2):
      for x in range(1,len(N)):
          for y in range(1,len(N)):
                n1 =N[x][0]
                n2= N[0][y]
                n1_i = vertices.index(n1)
                n2_i = vertices.index(n2)
                if distances[n1_i] + path_weight(n1,n2,N) < distances[n2_i]:
                    distances[n2_i] = distances[n1_i] + path_weight(n1,n2,N)
                    N[n1_i][n2_i] = distances[n1_i] + path_weight(n1,n2,N)
                    predecessors[n2_i] = n1
  print ("vertices: " + str(vertices))
  print ("corresponding predecessors: " + str(predecessors))
  print ("corresponding distances between them: " + str(distances))
  return (vertices,predecessors)

#given the set of vertices and their predecessors, generate edge pairs
#first element is the starting node, second is the ending node
def generate_edges(vert,pred):
    nodepairs=[]
    for i in range(0,len(vert)):
        nodepairs=nodepairs + [(pred[i],vert[i])]
    return nodepairs
    

#given a set of node pairs, for each 


def forw_table(source,goal,nodepairs):
  i=0
  while (nodepairs[i][1]!= goal):
      i=i+1
  if (nodepairs[i][0] == source):
      return (nodepairs[i][1])
  else:      
    return forw_table(source,nodepairs[i][0],nodepairs)
    

    
def main():
    N=create_adj_table()
    source = 'z'
    vertices,predecessors = Bellman_Ford(source,N)
    nodepairs = generate_edges(vertices,predecessors)
    print("Forwarding Table for node " +str(source))
    for i in range (1,len(N[0])-1):
        print (str(N[0][i])+ "      " + str(source)+ "      " + forw_table(source,N[0][i],nodepairs))  
        
main()
