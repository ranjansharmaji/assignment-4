import numpy as np
import matplotlib.pyplot as plt 

x1=np.random.rand(10000)
x2=np.random.rand(10000)
y1=np.sqrt(-2*np.log(x1))*np.cos(2*np.pi*x2)

plt.hist(y1,bins=25,density=True) 

xd=np.linspace(min(y1),max(y1)) 
yd=np.exp(-xd**2/2)/np.sqrt(2*np.pi) 

plt.plot(xd,yd,label='gaussian pdf')

plt.xlabel('random number')
plt.ylabel('density')

plt.legend()
plt.show() 