def nearestValidPoint(x,y,points):
    index=-1
    smallest=float('inf')
    i=0
    for apoint in points:
        a,b=apoint
        if(a==x or b==y):
            d=abs(a-x)+abs(b-y)
            if d<smallest:
                smallest,index=d,i
        i+=1
    return index

def nearestValidPoint2(x,y,points):
    index,smallest=-1,float('inf')
    for i,(a,b) in enumerate(points):
        dx,dy=x-a,y-b
        if dx*dy == 0 and abs(dx+dy)<smallest:
            smallest=abs(dx+dy)
            index=i
    return index
    

x = 3
y = 4
points = [[1,2],[3,1],[2,4],[2,3],[4,4]]

print(nearestValidPoint2(x,y,points))
