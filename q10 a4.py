import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

data="http://theory.tifr.res.in/~kulkarni/data.txt"

x=np.loadtxt(data,usecols=1,delimiter='&')
y=np.loadtxt(data,usecols=2,delimiter='&')
sigma_y=np.loadtxt(data,usecols=3,delimiter='&')

def log_likelihood(theta,x,y,yerr):
    a,b,c=theta
    model=a*x**2+b*x+c
    sigma2=sigma_y**2
    return np.sum((y-model)**2/sigma2+np.log(2*np.pi*sigma2))*0.5

def log_prior(theta):
    a,b,c=theta
    if -4000<a<4000 and -4000<b<4000 and -4000<c<4000:
        return 0
    return -np.inf

def log_probability(theta,x,y,sigma_y):
    lp=log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp-log_likelihood(theta,x,y,sigma_y)

guess=(1,1,1)
soln=minimize(log_likelihood,guess,args=(x,y,sigma_y))

nwalkers,ndim=50,3
pos=soln.x+1e-4*np.random.randn(nwalkers, ndim)

import emcee
sampler=emcee.EnsembleSampler(nwalkers,ndim,log_probability,args=(x,y,sigma_y))
sampler.run_mcmc(pos,5000)

samples=sampler.get_chain()




plt.plot(samples[:,:,0])
plt.xlabel('step number.')
plt.ylabel('a.')


plt.plot(samples[:,:,1])
plt.xlabel('step number.')
plt.ylabel('b')


plt.plot(samples[:,:,2])
plt.xlabel('step number.')
plt.ylabel('c')


plt.show()

































