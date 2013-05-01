import numpy as np

def fourPtFiniteDiff(x,y):
    """Uses a four point finite difference method to find the derivative of y with respect to x"""
    dydx = np.zeros(y.shape,float) #make the dimmension appropriate
    for j in range(2,len(y)-2):
        dydx[j] = (y[j-2]-8*y[j-1]+8*y[j+1]-y[j+2])/(12*(x[1]-x[0]))
    dydx[-1] = (y[-1]-y[-2])/(x[-1]-x[-2])
    dydx[-2] = (y[-2]-y[-3])/(x[-2]-x[-3])
    dydx[0] = (y[1]-y[0])/(x[1]-x[0])
    dydx[1] = (y[2]-y[1])/(x[2]-x[1])
    return dydx

def finiteDifference(x,y):
    """Uses a finite difference method to differentiate y with respect to x"""
    dydx = np.zeros(y.shape,float)
    dydx[:-1] = np.diff(y)/np.diff(x)
    dydx[-1] = (y[-1]-y[-2])/(x[-1]-x[-2])
    return dydx
