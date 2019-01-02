import random
import math

def getinp(str): #get the input in desired format(list of tuples)
    f=open("input.txt","r")
    f1=f.readlines()
    inp=[]
    for j in range(0,len(f1)):
        b=f1[j][1:-2]
        c=b.split('),(')
        b0=[]
        for i in c:
            x=i.split(',');
            temp=(int(x[0]),int(x[1]))
            #temp=[]
            #temp.append(int(x[0]))
            #temp.append(int(x[1]))
            b0.append(temp) 
        inp.append(b0)
    return inp

def point_inside_polygon(x, y, poly): #to check if sampled point inside obstacle
    n = len(poly)
    inside = False

    p1x, p1y = poly[0]
    for i in range(n + 1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y    
    return inside


def sample(): #to sample points
    x=random.randint(0,300)
    y=random.randint(0,200)
    #print(x,y)
    c=0
    for i in range(1,len(i1)-1):
        if(point_inside_polygon(x,y,i1[i])):
            c=1        
    if c==0:
        sp.append((x,y))


def dist(s,e): #distance between two points
    d = math.sqrt( (e[0] - s[0])**2 + (e[1] - s[1])**2 )
    return d

def line_intersection(line1, line2): #to check if two line segments intersect
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])
    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]
    div = det(xdiff, ydiff)
    if div == 0:
       return False
    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    if ((x<line1[0][0] and x>line1[1][0]) or (x>line1[0][0] and x<line1[1][0])):
        if((y<line1[0][1] and y>line1[1][1]) or (y>line1[0][1] and y<line1[1][1])):
            if ((x<line2[0][0] and x>line2[1][0]) or (x>line2[0][0] and x<line2[1][0])):
                if ((y<line2[0][1] and y>line2[1][1]) or (y>line2[0][1] and y<line2[1][1])):
                    return True
    return False


def poly_intersection(s,e): #to check if line intersects with an obstacle. Uses line_intersection
    for i in range(1,len(i1)-1):
        for k in range(0,len(i1[i])-1):
            if(line_intersection((s,e),(i1[i][k],i1[i][k+1]))):
                return False
            if(line_intersection((s,e),(i1[i][-1],i1[i][0]))):
                return False
    return True
                    

def kpoints(p,n): #find 3 nearest points or points upto distance 50(which ever is small)
    #print(p)
    d1=1000
    d2=1500
    d3=2000
    j1=0
    j2=0
    j3=0 
    for i in range(0,len(sp)):
        d=dist(p,sp[i])
        if d>0 and ((poly_intersection(p,sp[i]))):
            if d<d3:
                if d<d2:
                    if d<d1:
                        d1=d
                        j1=i
                    else:
                        d2=d
                        j2=i
                else:
                    d3=d
                    j3=i
    if d1<1000:
        e.append((n,j1))
        e1.append((p,sp[j1]))
    if d2<1500:
        e.append((n,j2))
        e1.append((p,sp[j2]))
    if d3<2000:
        e.append((n,j3))
        e1.append((p,sp[j3]))
    if(n==-11):
        e.append((j1,n))
        e.append((j2,n))
        e.append((j3,n))
        e1.append((sp[j1],p))
        e1.append((sp[j2],p))
        e1.append((sp[j3],p))
        
def nex(n): #to calculate next nodes on the path
    #ol.remove(n)
    cl.append(n)
    ol.remove(n)
    for i in range(0,len(e1)):
        if e1[i][0]==n and e1[i][1] not in cl:
            if (e1[i][1] not in ol) :
                ol.append(e1[i][1])

def path(s,e): # to calculate path
    path=[]
    path.append(s)
    m=s
    while True:
        #print(m)
        if m==e:
            path.append(m)
            return path
        nex(m)
        #if m == (-1,-1):
        if len(ol)>0:
            m=ol[-1]
        else:
            return []
        path.append(m)
        #if m==e:
        #    path.append(m)
        #    return path
        #ol.remove(m)

def oup():#to generate output file
    target=open("output.txt","w")
    l1=""
    for i in range(0,len(sp)):
        l1=l1+str(i)+" : "+str(sp[i])+","
    l2=""
    for i in range(0,len(e)):
        l2=l2+str(e[i])+","
    l3=""
    for i in range(0,len(p)):
        l3=l3+str(p[i])+","
    if len(p)==0:
        l3="No path as per our samples"
    target.write(l1)
    target.write("\n")
    target.write(l2)
    target.write("\n")
    target.write(l3)
    target.write("\n")
    target.close()

ol=[]
cl=[]
sp=[]
e=[]
e1=[]
fname=input("Enter input file name(eg. input.txt): ")
#fname="input1.txt"
i1=getinp(fname)
for i in range(1,1000):
    sample()
print("sampling done")
print("creating roadmap.please wait. This might take about 1-2 mins")
for m in range(0,len(sp)):
    kpoints(sp[m],m)
print("roadmap created. calculating path")
kpoints(i1[-1][0],-10)
kpoints(i1[-1][1],-11)
ol.append(i1[-1][0])
p=path(i1[-1][0],i1[-1][1])
oup()
print("done")



