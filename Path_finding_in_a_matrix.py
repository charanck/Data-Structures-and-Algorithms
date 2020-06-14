#"-" - denotes the available path
#[ , ,*,*,*,*,], - "- - * * * *"
#[*, ,*,*,*,*,], - "* - * * * *"
#[*, , ,*,*,*,], - "* - - * * *"
#[*,*, , , ,*,], - "* * - - - *"
#[*,*, ,*, ,*,], - "* * - * - *"
#[*,*, ,*, , ,]  - "* * - * - -"

import sys

n= int(sys.stdin.readline())
mat = []
for i in range(n):
    mat.append(sys.stdin.readline().strip().split())

final = None

def path(mat,x,y,p,n,visited):
    print("X= ",x,"Y= ",y)
    global final
    if((x,y) in visited or x == n or y== n or mat[x][y]=="*"):
        return False
    elif((x,y) == (n-1,n-1)):
        final = p
        p.append((5,5))
        p.remove((0,0))
        return True
    else:
        p.append((x,y))
        visited.append((x,y))
        if(path(mat,x+1,y,p,n,visited)):
            return True
        elif(path(mat,x,y+1,p,n,visited)):
            return True
        elif(path(mat,x-1,y,p,n,visited)):
            return True
        elif(path(mat,x,y-1,p,n,visited)):
            return True
        else:
            visited.pop()
            p.remove((x,y))
            return False
        

if(path(mat,0,0,[(0,0)],n,[])):
    print(final) 
else:
    print(False) 
    







