import random
import math

class SuperSorter:


   def __init__(self,lst1,lst2):
      self.lst1 = lst1
      self.lst2 = lst2
   
   def min_diff(self):
      lst=self.quick_sort(self.lst1)
      print(lst)
      min_dif = math.inf
      for i in range(0,len(lst)-1):
          if lst[i+1]-lst[i] < min_dif:
              a=lst[i+1]
              b=lst[i]
              min_dif=a-b    
      print(a)
      print(b)
      print(min_dif)


   def bubble_sort(self,lst):
       we_gud = False
       while (not(we_gud)):
           we_gud = True
           for i in range(0,len(lst)-1):
               if lst[i] > lst[i+1]:
                   x=lst[i]
                   y=lst[i+1]
                   lst[i+1]=x
                   lst[i]=y
                   we_gud=False
       return lst   

   def insertion_sort(self,lst):
       newlst=[lst[0]]
       for i in range(len(newlst),len(lst)):
           y=len(newlst)
           while lst[i] < newlst[y-1] and y > 0:
               y=y-1
           newlst.insert(y,lst[i])           
       print(newlst)
       return(newlst)


   def quick_sort(self,lst):
       if len(lst) < 2:
           return lst
       else:
           lstA = []
           lstB = []
           piv = random.randint(0,len(lst)-1)
           for e in lst:
               if e < lst[piv]:
                   lstA=lstA + [e]
               else:
                   lstB=lstB + [e]
       return (self.quick_sort(lstA) + self.quick_sort(lstB))


def main():
   lstA = [1,-3, 71, 68, -5, 16]
   lstB = [9,7,1,-4,2]
   lstC = [-26,20,-14,12,-13,2,-8]
   s=SuperSorter(lstC,lstB)
   print(s.bubble_sort(s.lst1))
   print(s.insertion_sort(s.lst2))
   print(s.quick_sort(s.lst1))
   s.min_diff()



main()
   


