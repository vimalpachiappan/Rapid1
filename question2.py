mylist = [1,2,3,5,8,4,7,9,1,4,12,5,6,5,2,1,0,8,1]
c={}

for i in mylist:
    b=0
    for j in mylist:
        if(i==j):
            b+=1
            c[i]=b
print(c)

            
 
