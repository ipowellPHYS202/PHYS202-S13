def pointPotential(X,Y,q,posx,posy):
    """docstring"""
    k=9*10**9
    return (k*q/((X-posx)**2+(Y-posy)**2)**(1/2.))

def dipolePotential(X,Y,q1,q2,d1,d2):
    return (pointPotential(X,Y,q1,-d1/2,-d2/2)+pointPotential(X,Y, q2, d1/2,d2/2))
