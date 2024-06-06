count = 0
ex,ey=[],[]
esize,espeed=[],[]
active=[]
over=False
px,py=0,0
psize=20
def setup():
    size(600,400)
def draw():
    global px,py,count,psize,over
    background(0)
    px=mouseX
    py=mouseY
    noStroke()
    fill(255)
    ellipse(px,py,psize,psize)

    
    if over:
        textAlign(CENTER)
        textSize(30)
        text("you fking noob",width/2,height/2)
        return
    
    count+=1
    if count%60==0:
        create()
    for i in range(len(active)):
        if active[i]:
            ex[i]+=espeed[i]
            if ex[i]<0 or ex[i]>width:
                espeed[i]*=-1
            noStroke()
            fill(255,0,0)
            ellipse(ex[i],ey[i],esize[i],esize[i])
            if is_hit(px,py,psize,ex[i],ey[i],esize[i]):
                if psize>esize[i]:
                    psize+=esize[i]*0.1
                    active[i]=False
                else:
                    over=True
            
def create():
    speed=int(random(-3,4))
    if speed==0:
        speed=1
    espeed.append(speed)
    if speed<0:
        ex.append(width)
    else:
        ex.append(0)
    ey.append(random(0,height))
    esize.append(random(psize*0.5,psize*2))
    active.append(True)
def is_hit(x1,y1,s1,x2,y2,s2):
    dis=dist(x1,y1,x2,y2)
    if dis<s1/2+s2/2:
        return True
    else:
        return False
        
    
    
    
    
