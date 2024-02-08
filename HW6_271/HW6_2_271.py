# comments fro problem 2
# in both a and b I used a single integral
# I am extremely unsure of my answer for 3
# I likely could have simplified the script with a singular function



from scipy import integrate
import math


#a

z=0.0
a=2.0
p=1.0
pi=math.pi

funt=lambda x: x**3

gral= integrate.quad(funt,0,a)

val1=4.0*pi*p*gral[0]

val_actual=(8*p*pi*a**5)/15

print(val1, " numerical")
print(val_actual, " analytical")



#b

a=0.7
p=1.0
b=1
pi=math.pi

funt2=lambda x: x**3
fak= lambda x: x**2

gral2= integrate.quad(funt,0,a)

val3=4.0*pi*p*gral[0]/2

gral3= integrate.quad(fak,0,b)

print(val3+gral[0]/3," icecream")

#c
height_of_plate=0.5
x=3
y=3

fua=lambda y,x: x**2

grock=integrate.dblquad(fua, -1.5, 1.5, -1.5, x)

print(grock[1]*height_of_plate)


