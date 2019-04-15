import matplotlib.pyplot as plt
import numpy as np
import math
#graphs the bending moment of tire swing from L (total length),
# b (length between supports), and W (weight of the tires)
def tireSwing(L,b,W):
    x1 = np.linspace(0, (L-b)*(1/2))
    x2 = np.linspace((L-b)*(1/2), (L/2))
    x3 = np.linspace((L/2), (1/2)*(L+b))
    x4 = np.linspace((1/2)*(L+b), L)
    y1 = -W*x1
    y2 = (W*x2)/2 + (3/4)*W*(b-L)
    y3 = W*(L/2-x3)/2 + W*(3*b/2-L)/2    
    y4 = -W*(L-x4)
    plt.grid()
    plt.xlim(-0.1,2.2)
    plt.ylim(-0.3,0.3)
    plt.xlabel('x')
    plt.ylabel('M(x)')
    plt.title('Tire Swing Bending Moment Diagram')
    plt.fill_between(x1,0,y1,color=(1,0.6,0))
    plt.fill_between(x2,0,y2,color=(1,0.6,0))
    plt.fill_between(x3,0,y3,color=(1,0.6,0))
    plt.fill_between(x4,0,y4,color=(1,0.6,0))
    plt.xticks([0.00,0.25,0.50,0.75,1.00,1.25,1.50,1,1.75,2.00])
    plt.yticks([-0.2,-0.1,0.0,0.1,0.2])
    plt.show()
#plots magnitudes of M+ and M- in terms of b
#from the parameters L and W
def optimalPlacement(L,W):
    b = np.linspace(0,2)
    Mpos = abs((1/2)*W*(3*b/2-L))
    Mneg = abs(-(1/2)*W*(L-b))
    plt.plot(b,Mpos,'r--',linewidth=3)
    plt.plot(b,Mneg,'y',linewidth=3)
    plt.xlim(0.0,2.0)
    plt.ylim(0.0,2.0)
    plt.grid()
    plt.xlabel('b(m)')
    plt.ylabel('M (N M)')
    plt.title('Bending Moment Resultant Maximal Value for Bending Leg Placements')
    plt.show()
#displays the strain and displacement fields for the bar using
#L (length), E (elastic modulus), P (tensile load), A0 (cross sectional
#area of small end)
def barStrain(L,A0,E,P):
    x = np.linspace(0,1.0)
    EofX = P/(E*A0*(2-(x/L)))
    UofX = ((P*L)/(E*A0))*np.log((2*L)/(2*L-x))
    plt.subplot(2,1,1)
    plt.plot(x,EofX,'r')
    plt.fill_between(x,0,EofX,color=(1.0,0,0))
    plt.grid()
    plt.ylabel('$\epsilon_a(x)$')
    plt.xlim(0.0,1.0)
    plt.ylim(0.000,0.016)
    plt.xticks([0.0,0.2,0.4,0.6,0.8,1.0])
    plt.yticks([0.000,0.002,0.004,0.006,0.008,0.010,0.012,0.014,0.016])
    plt.title('Axial strain field')
    plt.subplot(2,1,2)
    plt.plot(x,UofX,'b')
    plt.fill_between(x,0,UofX,color=(0.0,0.0,1.0))
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('$u_x(x)$')
    plt.xticks([0.0,0.2,0.4,0.6,0.8,1.0])
    plt.yticks([0.000,0.002,0.004,0.006,0.008,0.010,0.012])
    plt.xlim(0.0,1.0)
    plt.ylim(0.000,0.012)
    plt.title('Displacement field')
    plt.show()



























    
    
    
    
    

    




