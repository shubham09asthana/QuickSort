#SAMPLE Elements to test the sort
# 50 40 20 60 80 100 45 70 105 30 75

#Here,
#t is the Traversing pointer
# piv --> Pivot Element's index
#   x --> List storing user input
#   a --> The temporary list for computation
#   v --> Final Sorted list
def lr(a,piv):
    t=0
    while(a[t]<a[piv] and t!=piv): #loop will exit when left element is Greater than Pivot Element
        t+=1                       
    if(t==piv):
       #piv is at corrct position
      
       if(t>0):
           a[0:t]= rl(a[0:t],0)
      
       a[t+1:]=rl(a[t+1:],0)
    else:
        #swap(a[t],a[piv])
        a[t],a[piv]=a[piv],a[t]
        print(a," swaped ",a[t]," and ",a[piv])
        a=rl(a,t)
    return a
def rl(a,piv):
    t=len(a)-1
    
    if(len(a)<=1):
        
        return a
    
    while(a[t]>a[piv] and t!=piv):
        t-=1
     
    if(t==piv):
        #piv is at corrct position
      
       if(t>0): 
           a[0:t]= rl(a[0:t],0)
       
       a[t+1:]=rl(a[t+1:],0)
       
    else:
        #swap(a[t],a[piv])
        a[t],a[piv]=a[piv],a[t]
        print(a," swaped ",a[t]," and ",a[piv])
        a=lr(a,t)
    return a

z=input("Enter the Ele of list for Quick Sort : ")
x = list(map(int, z.split()))
v=rl(x,0)
print("sorted List is")
print(v)
