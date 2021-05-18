class User():

    Users = []

    def __init__(self,ID,friendList):
        self.ID = ID
        self.friendList = friendList
        User.Users=User.Users + [self]


    def determine_shortest_dis(x,y,c):
        if c > len(User.Users):
            return c
        if y.ID in x.friendList:
            return c 
        else:
            paths = []
            for e in x.friendList:
                cls=User.str_to_class(e)
                paths=paths + [User.determine_shortest_dis(cls,y,c+1)]
            if len(paths)==0:
                return None
            else:
                return min(paths)
            
    def str_to_class(string1):
        for e in User.Users:
            if e.ID == string1:
                return e


def main():
   
    a=User("a",["c","d"])
    b=User("b",["c", "a"])
    c=User("c",["d","b"])
    d=User("d",["a","e"])
    e=User("e",["c","a"])
    print(User.determine_shortest_dis(d,b,1))
    print(User.determine_shortest_dis(b,d,1))
    print(User.determine_shortest_dis(e,d,1))
 
main()
