import numpy as np 
import matplotlib.pyplot as plt 

a=1897
m=100
c=89887
x=1


n=10000
result=[] 

for i in range(n):
  x=(a*x+c)%m/100
  result.append(x)

xd=np.linspace(0,1)
yd=np.ones(len(xd))

plt.hist(result,bins=25,density=True)
plt.plot(xd,yd,label='uniform pdf.')

plt.xlabel('random number')
plt.ylabel('density')


plt.legend()
plt.show()