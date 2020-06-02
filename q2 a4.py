import numpy as np 
import matplotlib.pyplot as plt 

n=10000

result=np.random.rand(n)

xd=np.linspace(0,1)
yd=np.ones(len(xd))

plt.hist(result,bins=25,density=True)
plt.plot(xd,yd,label='uniform pdf')

plt.xlabel('random number')
plt.ylabel('density')


plt.legend()
plt.show()