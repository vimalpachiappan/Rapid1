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


i=0
while(i!=number):
        x=runs[i] 
        if(x in [1,3,5]):
         if(B1==0):
           S1=S1+runs[i]
           B1=0	
           B2=1
         elif(B2==0):
           S2=S2+runs[i]
           B1=1
           B2=0
        elif(x in [0,2,4,6]):
         if(B1==0):
           S1=S1+runs[i]
         elif(B2==0):
            S2=S2+runs[i]
        else:
              print("INVALID INPUT")
        i=i+1
        if(i in [6,12,18,24,30,36,42,48,54,60]):
          B1=not(B1)
          B2=not(B2) 

print("Batsman 1 score : "+str(S1))
print("Batsman 2 score : "+str(S2))
TOTAL=S1+S2
print("Total Score : "+str(TOTAL))

##########################################################

a = [2,1,0,4,2,2,6,4,3,6,1,2,0,2,6,1,3,2,6,1,4,3]
print("Total runs scored ", sum(a))
temp=[]
bat1=[]
bat2=[]

def split(k, size):
     j = []
     while len(k) > size:
         pice = k[:size]
         j.append(pice)
         k   = k[size:]
     j.append(k)
     return j

b = list(split(a,6))
print(b)
print(len(b))
for j in range(0,len(b)):
    for i in b[j]:
        if i%2==0:
            bat1.append(i)
            print('bat1',bat1)
            print('sum1',sum(bat1))
        else:
            bat2.append(i)
            print('bat2',bat2)
            print('bat2sum',sum(bat2))
