import math 
import planck
import numpy as np
import matplotlib.pyplot as plt


t_1=planck.radiance(3,1)

print("Actual Val" +"\n", t_1)

interp1=1
interp1_1= interp1+1

interp2=3
interp2_1=4

interp3=5
interp3_1=6


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

for r2 in range(0,interp_1):
    table2[0,r2]=planck.radiance(table[row-1,r2], 1)

    
table0=np.ones((1,interp_1))
    
   
for r3 in range(0,interp_1):
   
    table2[0,r3]=abs(table2[0,r3]-t_1)/t_1*100
print("\n",table2)

#plotting...
x1, y1 = zip(*linData)
x2, y2 = zip(*cubeData)
x3, y3 = zip(*quintData)

plt.loglog(x1, y1, color='r', label='linear approximation error')
plt.loglog(x2, y2, color='g', label='Cubic approximation error')
plt.loglog(x3, y3, color='b', label='Quintic approximation error')

#configuring the plot
plt.xlabel('Step size')
plt.ylabel('Error')
plt.title('Log-Log Plot of Error vs Step Size Centered')
plt.legend()

plt.show()