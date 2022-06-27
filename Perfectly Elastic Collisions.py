#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
import vpython as vp

A= 0.3
B= 0.1
m=0.1

y1=0
y2=0.2


r1= vp.vector(-5,y1,0)
r2= vp.vector(5,y2,0)
v1 = vp.vector(3,0,0)
v2= vp.vector(-3,0,0)
scene=vp.canvas()

red = vp.sphere (pos = r1, #initial position of the ball
                radius = 0.3,
                color = vp.color.red,
                vel = v1,
                 acel = vp.vector(0,0,0)) #initial velocity of the ball


blue = vp.sphere (pos = r2 , #initial position of the ball
                radius = 0.3,
                color = vp.color.blue,
                vel = v2,
                 acel = vp.vector(0,0,0))#initial velocity of the ball

vp.graph(title = 'F(r) vs r',
        xtitle = 'r',
         ytitle = 'F(r)')
rGraph= vp.gcurve(color = vp.color.green, label = 'Force vs Distance')

vp.graph(title = 'U(r) vs r',
        xtitle = 'r',
         ytitle = 'U(r)')
uGraph= vp.gcurve(color = vp.color.green, label = 'Potential Energy')

vp.graph(title = 'F(r) vs t',
        xtitle = 't',
         ytitle = 'F(r)')
tGraph= vp.gcurve(color = vp.color.green, label = 'Impulse')
gGraph=vp.gcurve(color=vp.color.blue)

vp.graph(title = 'F(r) vs r',
        xtitle = 'r',
         ytitle = 'F(r)')
kGraph= vp.gcurve(color = vp.color.green, label = 'Kinetic Energy')

vp.graph(title = 'F(r) vs r',
        xtitle = 'r',
         ymin=0,
         ymax=5,
         ytitle = 'F(r)')
mGraph= vp.gcurve(color = vp.color.green, label = 'Machenical Energy')



def F(r):
    F=((A/(vp.mag(r))**7)-(B/(vp.mag(r))**5))*vp.hat(r)
    return F



def U(r):
    U= A/(6*r.mag**6) - B/(4*r.mag**4)
    return U

def K(v1, v2):
    K= (m*v1**2)/2 + (m*v2**2)/2
    return K
    



J= vp.vector(0,0,0)
t=0
dt=0.0001
tmax=3
while t<tmax:
    
    vp.rate(3000)
    r=red.pos-blue.pos
    red.acel= F(r)/m
    blue.acel=-F(r)/m
    red.vel= red.vel + red.acel*dt
    blue.vel= blue.vel + blue.acel*dt
    red.pos= red.pos + red.vel*dt
    blue.pos=blue.pos +blue.vel*dt
    J= J + F(r)*dt
    t=t+dt

    
    
    
    rGraph.plot(r.mag, F(r).mag)
    tGraph.plot(t, F(r).mag)
    gGraph.plot(t,-F(r).mag)
    uGraph.plot(t, U(r))
    kGraph.plot(t, K(red.vel.mag, blue.vel.mag))
    mGraph.plot(t, K(red.vel.mag, blue.vel.mag)+U(r))
    
        
    
print(r)
print(J)
print(m*red.vel- m*v1)
print(m*blue.vel- m*v2)


# In[ ]:





# In[ ]:




