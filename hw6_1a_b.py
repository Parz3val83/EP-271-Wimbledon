
import matplotlib.pyplot as plt
import numpy as np

def solvefi(soln,r_t,r_s=0.05,sig_a=2.20,sig_s=345.0,mew=0.324):
    
    #the output of this function is a vector for fi
        
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
    
    rhs[0]=1
    rhs[nsys-1]=0.0002

    matr1[0,0]=1
        
    matr1[nsys-1,nsys-3]=-D/(2*h)
    matr1[nsys-1,nsys-2]=-4*D/(2*h)
    matr1[nsys-1,nsys-1]=3*D/(2*h)
    
    solut=np.linalg.solve(matr1,rhs)
    
    return(solut)



# main line
length=float(input("enter r_t value: "))
soln=int(input("enter amount of segments: "))
fi_r=solvefi(soln,length)


print(fi_r)


xvals=np.linspace(0.05,length+1,len(fi_r))
yvals=fi_r
plt.figure(0.05,figsize=[6.,4.])
plt.subplots_adjust(left=0.17,bottom=0.13,right=0.95,top=0.95)
plt.plot(xvals,fi_r,'k',linewidth=2)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Radious r',fontsize=13)
plt.ylabel('fi_r',fontsize=13)



length= 0.1
soln=[16,32,64,128]

    
plt.figure(figsize=[6.,4.])
plt.subplots_adjust(left=0.17,bottom=0.13,right=0.95,top=0.95)


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
   