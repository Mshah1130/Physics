#!/usr/bin/env python
# coding: utf-8

# # Numerical Integration

# In[5]:


import matplotlib.pyplot as plt
import numpy as np

m = 0.45 # soccer ball mass in kg
g = 9.81 # force of gravity

#create arrays to populate a, y, v and a values for plotting purposes
tValues = []
yValues = []
vValues = []
aValues = []


def Fnet(v): # function that returns F
    k = 0.02 # 1/m
    F = -m*g + k*v**2
    
    return F

# Start the numerical integration
y = 100    #initial height of the soccer ball in meters
v = 0      #initial velocity of the soccer ball

t = 0      #initial time in seconds
dt = 0.1   #delta t in seconds

while y > 0: #condition is false once the ball hits the ground
    a = Fnet(v)/m              #for the t time interval find acceleration 
    y = y + v*dt + 1/2*a*dt**2 #for the t time interval find position
    v = v + a*dt               #for the t time interval find velocity
    
    tValues.append(t)
    yValues.append(y)
    vValues.append(v)
    aValues.append(a)

    t = t + dt
    
plt.title("Height vs Time")    #plt permits you to use library matplotlib
plt.ylabel("y (m)")
plt.xlabel("t (s)")
plt.plot(tValues, yValues, 'b')
plt.show()  #permits showing in separate graphs

plt.title("Velocity vs Time")
plt.ylabel("v (m)")
plt.xlabel("t (s)")
plt.plot(tValues, vValues, 'b')
plt.show()

plt.title("Acceleration vs Time")
plt.ylabel("a (m)")
plt.xlabel("t (s)")
plt.plot(tValues, vValues, 'b')
plt.show()


# In[ ]:





# In[ ]:




