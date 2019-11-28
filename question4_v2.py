number=input("enter the number of array values : ")
runs=[]
for i in range(int(number)):
	n=input('number : ')
	runs.append(int(n))

print(runs)
B1=0
B2=1
S1=0
S2=0
TOTAL=0
global z

z=0
number=int(number)
while(z!=number):
        

        x=runs[z]  
        print(x)
        if(x in [1,3,5]):
         if(B1==0):
           S1=S1+x
           B1=1	
           B2=0
         elif(B2==0):
           S2=S2+x
           B1=0
           B2=1
        elif(x in [0,2,4,6]):
         if(B1==0):
           S1=S1+x
         elif(B2==0):
            S2=S2+x
        
        z=z+1
        
        if(z in [6,12,18,24,30,36,42,48,54,60]):
          B1=not(B1)
          B2=not(B2) 


print("Batsman 1 score : "+str(S1))
print("Batsman 2 score : "+str(S2))
TOTAL=S1+S2
print("Total Score : "+str(TOTAL))
