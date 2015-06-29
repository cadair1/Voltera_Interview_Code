import math
def GetYpoint(x,tuple_x,tuple_y):
        slope = (tuple_y[1]-tuple_y[0])/(tuple_x[1]-tuple_x[0])
        b = tuple_y[1] - slope*tuple_x[1]
        y = slope*x + b
        return y;

class Polygon:
    def __init__(self, xlist, ylist):
        self.xpoints = xlist
        self.ypoints = ylist
        
    def AddPoint(self,x,y):
        self.xpoints.append(x)
        self.ypoints.append(y)
        
    def PointInPolygon (self,x,y):
        numpoints = len(self.xpoints)
        xpairs = []
        ypairs = []
        for pointnum in range(numpoints):
            if x <= self.xpoints[pointnum] and x>=self.xpoints[(pointnum+1)%numpoints]:
                a = (self.xpoints[pointnum],self.xpoints[(pointnum+1)%numpoints])
                b = (self.ypoints[pointnum],self.ypoints[(pointnum+1)%numpoints])
                xpairs.append(a)
                ypairs.append(b)
            elif  x >= self.xpoints[pointnum] and x<=self.xpoints[(pointnum+1)%numpoints]:
                a = (self.xpoints[pointnum],self.xpoints[(pointnum+1)%numpoints])
                b = (self.ypoints[pointnum],self.ypoints[(pointnum+1)%numpoints])
                xpairs.append(a)
                ypairs.append(b)
        if xpairs == []:
            print 'Point is not in the Polygon'
            return False
        print xpairs
        if len(xpairs)>2: #Eliminate Vertical x and y pairs
            xpairs_2 = []
            ypairs_2 = []
            for pairnum in range(len(xpairs)):
                if xpairs[pairnum][0] != xpairs[pairnum][1]:
                    xpairs_2.append(xpairs[pairnum])
                    ypairs_2.append(ypairs[pairnum])
            xpairs = xpairs_2
            ypairs = ypairs_2
        if len(xpairs) > 2:
            xpairs_3 = []
            ypairs_3 = []
            for pairnum in range(len(xpairs)):
                if xpairs[pairnum][1] != xpairs[(pairnum+1)%len(xpairs)][0] and xpairs[pairnum][0] != xpairs[(pairnum+1)%len(xpairs)][1]:
                    xpairs_3.append(xpairs[pairnum])
                    xpairs_3.append(xpairs[(pairnum+1)%len(xpairs)])
                    ypairs_3.append(ypairs[pairnum])
                    ypairs_3.append(ypairs[(pairnum+1)%len(ypairs)])
                    break
            xpairs = xpairs_3
            ypairs = ypairs_3   
        y_1 = GetYpoint(x,xpairs[0],ypairs[0])
        y_2 = GetYpoint(x,xpairs[1],ypairs[1])
        if y_1 <= y_2:
            if y >=  y_1 and y<= y_2:
                print 'Point is in the Polygon'
                return True;
            else:
                print 'Point is not in the Polygon'
                return False;
        elif y_2 <= y_1:
                if y>= y_2 and y<= y_1:
                    print 'Point is in the Polygon'
                    return True;
                else:
                    print 'Point is not in the Polygon' 
                    return False;
                
class RegularOctagon(Polygon):
    def __init__(self,d):
        angle = math.pi/4.0
        xlist = []
        ylist = []
        for x in xrange(8):
            xlist.append(d*math.cos(x*angle))
            ylist.append(d*math.sin(x*angle))
        Polygon.__init__(self,xlist,ylist)
                
Test_one = Polygon([1.0,-1.0,-1.0,1.0],[1.0,1.0,-1.0,-1.0])
test_two = RegularOctagon(1)
#Test_one.PointInPolygon(-1.0,1.5)
#test_two.PointInPolygon(0.5,0.5)
