import numpy as np
import matplotlib.pyplot as plt 

x=20*np.random.rand(10000)
y=np.random.rand(10000) 

def f(x):
  return np.exp(-x**2/2)/np.sqrt(np.pi/2) 

xgood=x[y<f(x)];ygood=y[y<f(x)]

plt.hist(xgood,density=True) 

xd=np.linspace(min(xgood),max(xgood)) 
yd=np.exp(-xd**2/2)/np.sqrt(np.pi/2)  

plt.plot(xd,yd,label='gaussian pdf')

plt.xlabel('random number')
plt.ylabel('density')

plt.legend()
plt.show() 