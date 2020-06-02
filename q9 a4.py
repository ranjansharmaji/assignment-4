import numpy as np 
import matplotlib.pyplot as plt 

nsteps=1000
theta=3

def f(x):
  if 3<=x<=7:
    return 1
  else:
    return 0
    
k=[]
x=[]

for i in range(nsteps):
  theta_prime=theta+np.random.standard_normal() 
  r=np.random.rand()
  if (f(theta)>0)and(f(theta_prime)/f(theta)>r):
    theta = theta_prime
  k.append(theta)
  x.append(i)



plt.subplot(211)
plt.plot(x,k)
plt.xlabel('step')
plt.ylabel('theta.')



plt.subplot(212)
plt.hist(k,density=True)
plt.xlabel('random numbers.')
plt.ylabel('density.')
 

plt.show() 