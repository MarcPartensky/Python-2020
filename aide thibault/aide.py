import numpy as np

k = lambda x:3*np.sin(x)*np.exp(np.sqrt(x))/(2*x)

def cordes_para(f,x0,epsilon,gamma,maxiter=50):
  xn = x0
  for i in range(maxiter):
    xn_ = xn
    xn = xn-f(xn)/gamma
    print(xn, f(xn))
  return (xn, np.abs(xn_-xn)<epsilon)

print(cordes_para(lambda x:k(x)-0.25, 3.5, 1, 5))
