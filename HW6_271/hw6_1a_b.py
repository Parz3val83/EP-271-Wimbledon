"""
My answere for part c is r_t = 25.4236
The plot for part b looks odd, but I believe it to be correct
it would make sense that h is constant

For part a it would also make sense that the desity of the 
particle is closest to the source

There were some negative values which I was unsure of how to intepret

""""
import matplotlib.pyplot as plt
import numpy as np

def solvefi(soln,r_t,r_s=0.05,sig_a=2.20,sig_s=345.0,mew=0.324):

    #soln is the value of n
    #r_t is r_t
    #the rest of the variables are constants
        
    nsys=soln
    matr1=np.zeros((nsys,nsys))
    rhs=np.zeros(nsys)
    
    #establish variables in equation
    D=1/3*(sig_a+sig_s*(1-mew))
    h=r_t/(nsys-1)


    #for loop to create matrix of lhs p1
    
    for i in range(1,nsys-1):
        
        
        matr1[i,i-1]=-D*(i-1/2)/h        #  M_(i,i-1)
        matr1[i,i]=2*i*D/h+sig_a*i*h     #  M_(i,i)* what about fi_of r?
        matr1[i,i+1]=-D*(i+1/2)/h     #  M_(i,i+1)
        
        i+=1
    
    # adjsut 0,0 and rhs firt position or fi of r_s
    rhs[0]=1
    matr1[0,0]=1
    
    #edit last row for boundary condtion
    matr1[nsys-1,nsys-3]=-D/(2*h)
    matr1[nsys-1,nsys-2]=-4*D/(2*h)
    matr1[nsys-1,nsys-1]=3*D/(2*h)
    
    #solve using linalge funtion
    solut=np.linalg.solve(matr1,rhs)
    
    #return the solution
    return(solut)



# main 

#enter r_t and n conditions
length=float(input("enter r_t value: "))
soln=int(input("enter amount of segments: "))

# use funtion
fi_r=solvefi(soln,length)


print(fi_r)

# ploting
xvals=np.linspace(0.05,length+1,len(fi_r))
yvals=fi_r
plt.figure(0.05,figsize=[6.,4.])
plt.subplots_adjust(left=0.17,bottom=0.13,right=0.95,top=0.95)
plt.plot(xvals,fi_r,'k',linewidth=2)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Radious r',fontsize=13)
plt.ylabel('fi_r',fontsize=13)


# part b

#length is r_t
length= 0.1
soln=[16,32,64,128]

    
plt.figure(figsize=[6.,4.])
plt.subplots_adjust(left=0.17,bottom=0.13,right=0.95,top=0.95)

# loop through all of n's and plot
for i in soln:
    fi_r=solvefi(i,length)
    h=0.05/i
    
    plt.plot(fi_r,np.full_like(fi_r,h))
    

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.xlabel('fi_r',fontsize=13)
plt.ylabel('h',fontsize=13)    
plt.legend(['16','32','64','128'])
plt.show
   