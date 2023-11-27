import math 
import planck
import numpy as np

t_1=planck.radiance(3,1)

print("Actual Val" +"\n", t_1)

interp=int(input("enter your interpolattion degree: "))
interp_1= interp+1
row = int(input("user input of precission: "))

freq = 3
dim = ((row,interp_1))
table= np.ones(dim)

frac= 0.5


for i in range(0,row): #row  
    initial=freq-frac
    
    for r in range(0,interp_1): # collumn
        if r==0:
           table[i,r]=initial
        else:
            table[i,r]= initial + 2*frac*r
    
    frac*=1/2
    i+=1
    
print("\n" + "Data to precision " + str(interp) +"\n",table)

#finding and ploting error
table2=np.ones((1,interp_1))

print(table2)

for r2 in range(0,interp_1):
    table2[0,r2]=planck.radiance(table[row-1,r2], 1)
    
print(table2)