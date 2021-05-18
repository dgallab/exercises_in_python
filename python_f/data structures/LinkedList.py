class Node():

    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None  #this will be another node


class LinkedList():

    def __init__(self):
        self.headval = None #this will be a node, not a datavalue

    def add_node(self,node):
        if self.headval is None:
            self.headval = node
        else:
            x=self.headval
            while x.nextval is not None:
                x=x.nextval
            x.nextval = node

    def remove_node(self, val):
        x=self.headval
        if (x is not None) and (x.dataval == val):
            self.headval = x.nextval
            x=None    
        else:
            y=x.nextval
            while (x is not None):
                if y.dataval == val:
                   x = y
                   y = y.nextval
                break
                    
            if x == None:
                return
            x.nextval=y.nextval
            x=None
            
            
       
                
        
    
    def print_LL(self):
         cn = self.headval
         while cn is not None:
             print(cn.dataval)
             cn=cn.nextval
    

def main():
    a=Node("a")
    b=Node("b")
    c=Node("z")
    LL = LinkedList()
    LL.add_node(a)
    LL.add_node(b)
    LL.add_node(c)
    LL.print_LL()
    print('\n')
    LL.remove_node("z")
    LL.print_LL()
    
main()
