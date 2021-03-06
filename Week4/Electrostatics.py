def pointPotential(X,Y,q,posx,posy):
    """docstring"""
    k=9*10**9
    return (k*q/((X-posx)**2+(Y-posy)**2)**(1/2.))

def dipolePotential(X,Y,q1,q2,d1,d2):
    return (pointPotential(X,Y,q1,-d1/2,-d2/2)+pointPotential(X,Y, q2, d1/2,d2/2))

def E_x(x,y,q,Xq,Yq):
    k=8.99*10**9
    return k*q*(x-Xq)/((((x-Xq)**2)+((y-Yq)**2))**1./2.)
    
def E_y(x,y,q,Xq,Yq):
    k=8.99*10**9
    return k*q*(y-Yq)/((((x-Xq)**2)+((y-Yq)**2))**1./2.)
    
def pointField(x,y,q,Xq,Yq):
    """Returns the value of the electric field components due to a point charge at (Xq,Yq) at specific location x,y with charge q"""
    return (E_x(x,y,q,Xq,Yq), E_y(x,y,q,Xq,Yq))
