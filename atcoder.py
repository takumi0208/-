import random as r
c=[2,4,6,7,8,10,11,13,15,16,18,19]
b=20
ans=True
def f(a):
    p=len(a)
    for k in range(p):
        print(*a[k])
    return


a=[['□']*b for i in range(b)]
for i in range(20):
    g=r.sample(c,7)
    for j in range(7):
        a[i][g[j]]='■'
x,y=0,0  
a[x][y]='P'
a[19][19]='G'

while ans:
    try:
        f(a)
        idou=str(input('wは上dは右sは下aは左'))
        if idou == 'w' and a[x-1][y]!='■':
            c,t=x,y
            a[x][y]='□'
            x-=1
            x=max(0,x)
            a[max(0,x)][y]='P'
            if x==19 and y==19:
                print('クリア')
                ans=False
        elif idou == 'd' and a[x][y+1]!='■':
            c,t=x,y
            a[x][y]='□'
            y+=1
            a[x][y]='P'
            if x==19 and y==19:
                print('クリア')
                ans=False

        elif idou == 's' and a[x+1][y]!='■':
            c,t=x,y
            a[x][y]='□'
            x+=1
            a[x][y]='P'
            if x==19 and y==19:
                print('クリア')
                ans=False

        elif idou == 'a' and a[x][y-1]!='■':
            c,t=x,y
            a[x][y]='□'
            y-=1
            y=max(0,y)
            a[x][max(0,y)]='P'
            if x==19 and y==19:
                print('クリア')
                f(a)
                ans=False
    except:
            c,t=x,y
            a[c][y]='P'