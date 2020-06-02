import numpy as np

n=100000 


x=np.random.rand(n)-1
y=np.random.rand(n)-1

k=0 
for i in range(n):
  if x[i]**2+y[i]**2<=1:
    k+=1
Area=2**2*(k/n) 
print('area of circle',Area)



a=np.random.rand(n)-1
b=np.random.rand(n)-1
c=np.random.rand(n)-1
d=np.random.rand(n)-1
e=np.random.rand(n)-1
f=np.random.rand(n)-1
g=np.random.rand(n)-1
h=np.random.rand(n)-1
i=np.random.rand(n)-1
j=np.random.rand(n)-1

l=0 
for k in range(n):
  if a[k]**2+b[k]**2+c[k]**2+d[k]**2+e[k]**2+f[k]**2+g[k]**2+h[k]**2+i[k]**2+j[k]**2<=1:
    l+=1
V=2**10*(l/n) 
print('10d sphere volume',V) 