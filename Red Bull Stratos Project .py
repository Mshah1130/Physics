#!/usr/bin/env python
# coding: utf-8

# # Numerical Integration

# In[3]:


"""This project was inspired by the Redbull Stratos project which invoved Austrian skydiver 
Felix Baumgartner jumping from a height of nearly 127952.756 Ft, breaking multiple world record"""


#objective
#To calulate and visualize physics of man falling from the height of 40000ft. 

import matplotlib.pyplot as plt
import numpy as np

m = 118 # Mass of the man jumping in Kg 
g = 9.81 # force of gravity
c = 1 # Coefficient
A = 1 # Cross-sectional area
#create arrays to populate a, y, v and a values for plotting purposes
tValues = []        # time array
hValues = []        # height array
vValues = []        # velocity array
aValues = []        # acceleration array

def Rho(h):                   # This function find the value of Rho(p) over the height.
    M = 0.0289644
    R = 8.31447
    p0= 101325
    L = 0.0065
    T0= 288.15
    g = 9.8

    
    T=T0 - (L*h)    #T = T0 – L h
    
    p = p0*(1-(L*h/T0))**((g*M)/(R*L))  # p = p0 (1 – L h /T0)^g M /(R L)   

    return (p*M)/(R*T)    #ρ(h) = p M / (R T),


def Fnet(v,h): # This function return the net force on the man by subtraction Gravitialnal force with drag force
    k =  (c*Rho(h)*A)/2  #Combining all the constants of drag force.
    F = -m*g + k*v**2  
    
    return F



# Start the numerical integration
h = 38969    #initial height of the soccer ball in meters
v = 0      #initial velocity of the soccer ball

t = 0      #initial time in seconds
dt = 0.1   #delta t in seconds

while h > 0: #condition is false once the ball hits the ground
    a = Fnet(v,h)/m              #for the t time interval find acceleration 
    h = h + v*dt + 1/2*a*dt**2 #for the t time interval find position
    v = v + a*dt               #for the t time interval find velocity
    
    tValues.append(t)
    hValues.append(h)
    vValues.append(v)
    aValues.append(a)

    t = t + dt
    
    if abs(t-260) < 0.01 :  
        print(t,v)
    
    
        
    
            
    
    
    
plt.title("Height vs Time")    #plt permits you to use library matplotlib
plt.ylabel("h (m)")
plt.xlabel("t (s)")
plt.plot(tValues, hValues, 'b')
plt.scatter([34,50,64,180,260],[33446,27833,22960,7619,2567], color='red')
plt.show()


plt.title("Velocity vs Time")
plt.ylabel("v (m)")
plt.xlabel("t (s)")
plt.plot(tValues, vValues, 'b')
plt.scatter([34,50,64,180,260],[-309,-377,-289,-79,-53], color='red')
plt.show()  #permits showing in separate graphs



plt.title("Acceleration vs Time")
plt.ylabel("a (m)")
plt.xlabel("t (s)")
plt.plot(tValues, aValues, 'b')
plt.show()

print(t)




# Time of flight = 344.3s 
""" C. As the person is in freefall, velocity gets bigger which causes drag force to get bigger. 
Eventually drag force overcomes wieght and we have positive acceleration, 
velocity is getting smaller which causes drag force to get smaller. this happens until drag force gets equal to wieght force. 
At that instance we have terminal velocity. And net force is Fnet= 0"""
#s = 53.77527633018703m  at t= 260s Speed is 53m/s just before the parachute is deployed. 








# In[ ]:





# In[ ]:




