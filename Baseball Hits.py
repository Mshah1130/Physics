#!/usr/bin/env python
# coding: utf-8

# In[5]:


import math
import matplotlib.pyplot as plt
import numpy as np
import vpython as vp

m = 0.145 # ball mass in kg
C= 0.3 # Coefficient
A = 0.0043 # Cross-sectional area
p = 1.2 #density at sea level
h = 1.24 #initial height of baseball
v0= 19.22  #Initial Velocity of the baseball
Angle = 60   #Initial angle in degrees

theta = math.radians(Angle)

Vx=v0*math.cos(theta)

Vy=v0*math.sin(theta)

v = vp.vector (Vx,Vy,0)
v2 = vp.vector (Vx,Vy,0)

g = vp.vector(0,-9.81,0)


scene= vp.canvas()

floor = vp.box(pos = vp.vector(0, 0, 0),
              size= vp.vector(20, .2, 5),
              color = vp.color.green)

ball = vp.sphere (pos = vp.vector (0, 1 , 0), #initial position of the ball
                radius = 0.037,
                color = vp.color.blue,
                vel = v,
                 acel = vp.vector(0,0,0), make_trail=True) #initial velocity of the ball


balltwo = vp.sphere (pos = vp.vector (0, 1 , 0), #initial position of the ball
                radius = 0.037,
                color = vp.color.red,
                vel = v2,
                 acel = g, make_trail=True) #initial velocity of the ball

vp.graph(title = 'Acceleration vs Time',
        xtitle = 'Time (s)',
         ytitle = 'Acceleration(m/s^2)')
aGraph= vp.gcurve(color = vp.color.green, label = 'Ball Acceleration')

vp.graph(title = 'Velocity vs Time',
        xtitle = 'Time (s)',
         ytitle = 'Velocity(m/s)')
vGraph= vp.gcurve(color = vp.color.green, label = 'Ball velocity')




def Fnet(v):
    k= (C*A*p)/2
    F = -k*(ball.vel.mag**2)*(ball.vel.hat)+(m*g)
    return F

print(g)

print(ball.vel.mag)
print(ball.vel.hat)
print(Fnet(v))

print(ball.acel)


t=0
tmax=5
dt=0.01 



while balltwo.pos.y > 0 :
    vp.rate(100)
    
    ball.acel = Fnet(v)/m
    
    ball.vel = ball.vel + ball.acel*dt
    
    ball.pos = ball.pos + ball.vel*dt
    
    balltwo.vel = balltwo.vel + balltwo.acel*dt
    balltwo.pos = balltwo.pos + balltwo.vel*dt
    
    t=t+dt
    
    
    aGraph.plot(t,ball.acel.y)
    vGraph.plot(t, ball.vel.y)
    
print(ball.pos)




# In[3]:





# In[ ]:





# In[ ]:




