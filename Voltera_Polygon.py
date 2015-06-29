import math

# Given a pair of points in the cartesian plane the function finds the line connecting these points
#It then finds the y-value corresponding to a given input x value and returns the y value
#x-value is a float, x-tuple is a pair of floats, y-tuple is a pair of floats
def GetYpoint(x,tuple_x,tuple_y):
        slope = (tuple_y[1]-tuple_y[0])/(tuple_x[1]-tuple_x[0])
        b = tuple_y[1] - slope*tuple_x[1]
        y = slope*x + b
        return y;

class Polygon:
    def __init__(self, xlist, ylist): #Polygon is initialized with a list of x and y points (floats). 
        #It is assumed that the last x and y points in the list connect back to the first x and y points in the list
        #Points are connected by a straight line in the cartesian plane 
        # Assumed: len(xlist) == len(ylist) type(xlist[i]) == float, type(ylist[i]) == float
        self.xpoints = xlist
        self.ypoints = ylist
        
    def AddPoint(self,x,y): #Adds point to the polygon
        self.xpoints.append(x)
        self.ypoints.append(y)
        
    def pointInPolygon (self,x,y):
        #x and y form a point in the cartesian plane
        numpoints = len(self.xpoints)
        xpairs = []
        ypairs = []
        #We will get all the pairs of x points that are given x point falls between we check adjacent x points in our xlist
        #We also keep track of the corresponding y-pairs
        #can think of the x-pairs as \Delta x and y-pairs as \Delta y
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
        if xpairs == []: #If our x value is not between any sets of adjacent x-points it is either to the right or left of the polygon
            print 'Point is not in the Polygon'
            return False
        print xpairs
        if len(xpairs)>2: #Eliminate Vertical x and y pairs since they will mess up the GetYpoint function
            xpairs_2 = []
            ypairs_2 = []
            for pairnum in range(len(xpairs)):
                if xpairs[pairnum][0] != xpairs[pairnum][1]:
                    xpairs_2.append(xpairs[pairnum])
                    ypairs_2.append(ypairs[pairnum])
            xpairs = xpairs_2
            ypairs = ypairs_2
        #We have found all the x-pairs the bound the x-value of our point. Now we need to find a a pair of x-pairs that potentially bound
        #Bound the y point. We select any two x-pairs that dont share a common point.
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
        #We find the y point on our line connecting each pair that has our x value
        y_1 = GetYpoint(x,xpairs[0],ypairs[0])
        y_2 = GetYpoint(x,xpairs[1],ypairs[1])
        # Now we check if our y value is between the two y points of the two lines
        #If so then our point is in the polygon
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
        #The Regular Octagon class creates an octagon by finding the points of an octagon that lie on a circle of radius d
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
