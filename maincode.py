import random as rnd
import matplotlib.pyplot as plt
import numpy as np

class ball:
    'Ball class, store ball position and velocities'
    count=0
    
    def __init__(self,**arg):
        if 'x' in arg.keys():
            self.x=arg['x'];
        else:
            self.x=rnd.randrange(0,100,1);
        
        if 'y' in arg.keys():    
            self.y=arg['y'];
        else:
            self.y=rnd.randrange(0,100,1);

        if 'r' in arg.keys():    
            self.r=arg['r'];
        else:
            self.r=1;
         
        if 'vx' in arg.keys():        
            self.vx=arg['vx'];
        else:
            self.vx=rnd.randrange(-10,10,1);
        
        if 'vy' in arg.keys():
            self.vy=arg['vy'];
        else:
            self.vy=rnd.randrange(-10,10,1);
        
        ball.count+=1;
     
     
    def show(self):
        print "x,y,vx,vy: ",self.x,self.y,self.vx,self.vy
    
    def plot(self):
        plt.scatter(self.x,self.y)
        plt.show()
    def updatePosition(self,t,L):
        xmin,xmax,ymin,ymax=L;
        xnew=self.x+self.vx*t;
        ynew=self.y+self.vy*t;

        if xnew>xmax: xnew=2*xmax-xnew;self.vx=-self.vx;
        if xnew<xmin: xnew=2*xmin-xnew;self.vx=-self.vx;
        if ynew>ymax: ynew=2*ymax-ynew;self.vy=-self.vy;
        if ynew<ymin: ynew=2*ymin-ynew;self.vy=-self.vy;

        self.x=xnew;
        self.y=ynew;
        return
########### End of classes ####################    
  
def checkCollision(a,b):
    return pow(pow(a.x-b.x,2)+pow(a.y-b.y,2),0.5)<(a.r+b.r)

def collisionUpdate(a,b):
    c=((a.vx-b.vx)*(a.x-b.x)+(a.vy-b.vy)*(a.y-b.y))/(pow(a.x-b.x,2)+pow(a.y-b.y,2));
    a.vx=a.vx-c*(a.x-b.x);
    a.vy=a.vy-c*(a.y-b.y);

    b.vx=b.vx+c*(a.x-b.x);
    b.vy=b.vy+c*(a.y-b.y);
    return a,b;                      
########### End of functions ####################



N=50
b=[ball() for k in range(0,N)]
t=0.1
boundary=(0,100,0,100)
CYCLE=500;


for cycle in range(0,CYCLE):
    for m in range(0,N-1):
        for n in range(m+1,N):
            collision=checkCollision(b[m],b[n])
            
            if collision:
                b[m],b[n]=collisionUpdate(b[m],b[n])
                continue
    
    for k in range(0,N):
        b[k].updatePosition(t,boundary);
    
    data=np.zeros((N,2))            
    for k in range(0,N):
        data[k,]=b[k].x,b[k].y
    
    #data=np.append(data,[[0,0],[0,100],[100,0],[100,100]],axis=0)
    plt.hold(False)
 
    plt.scatter(data[:,0],data[:,1])
    plt.axis([-1,101,-1,101])
    plt.pause(0.0000001)