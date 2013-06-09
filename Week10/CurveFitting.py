import numpy as np
from math import sqrt
def LinearLeastSquaresFit(x,y):
    """takes arrays of (x,y) values of  linearly varying data and
    perform a linear least squares approximation. Return the resulting slope and y-intercept
    parameters of the best fit like with their corresponding  uncertainties."""
    n = np.double(len(x))
    x_ = np.mean(x)
    y_ = np.mean(y)
    x2_ = np.mean(x**2)
    xy_ = np.mean(x*y)
    m = (xy_ - (x_*y_))/(x2_ - (x_**2))
    b = ((x2_*y_) - (x_*xy_))/(x2_ - (x_**2))
    delta = y-(m*x + b)
    d2_ = np.mean(delta**2)
    sig_m = sqrt((1/(n-2))*(d2_/(x2_ - (x_**2))))
    sig_b = sqrt((1/(n-2))*((d2_*x2_)/(x2_ - (x_**2))))
    return m,b,sig_m,sig_b
