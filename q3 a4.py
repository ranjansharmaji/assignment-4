import time as t 
import numpy as np 


n=10000

t1=t.perf_counter()
result=np.random.rand(n)
t2=t.perf_counter()
print('time numpy',t2-t1)

a=1897
m=100
c=89887
x=1

result2=[]

t3=t.perf_counter()
for i in range(n):
  x=(a*x+c)%m/100
  result2.append(x)
t4=t.perf_counter()
print('time lcg',t4-t3)