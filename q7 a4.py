import numpy as np
from scipy.stats import chi2 

n=144 
nps=n*np.array([1,2,3,4,5,6,5,4,3,2,1])/36

y1=[4,10,10,13,20,18,18,11,13,14,13]
y2=[3,7,11,15,19,24,21,17,13,9,5]

v1=sum((y1-nps)**2/nps)
v2=sum((y2-nps)**2/nps)

p1=1-chi2.cdf(v1,10)
p2=1-chi2.cdf(v2,10)

print(p1,p2)

#0.0010368888967215995 0.999685063315782 what we get
#1st below 0.01 2nd greater then 0.99

# so both case "not sufficiently random"