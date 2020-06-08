v=[0,60,100,120]
vw=[0,10,20,30]
w=[0,10,20,30,40,50]
m = 50
dt=[[0 for j in range((m//10)+1)] for i in range(len(v))]
def dp(i,j,v,w,vw,dt):
    if i == 0 or j == 0:
        if i == 0:
            dp(i+1,0,v,w,vw,dt)
        else:
            dp(i,j+1,v,w,vw,dt)
    else:
        try:
            if(i > 3):
                return
            if(j>5):
                dp(i+1,0,v,w,vw,dt)
                
            if vw[i] <= w[j]:
                temp = v[i]
                if vw[i] - w[j] == 0:
                    dt[i][j] = temp
                    if(dt[i-1][j]>dt[i][j]):
                        dt[i][j] = dt[i-1][j]
                    if i == len(v)+1:
                        return
                    if j == 5:
                        dp(i+1,0,v,w,vw,dt)
                    else:
                        dp(i,j+1,v,w,vw,dt)
                else:
                    rem = (w[j]-vw[i])//10
                    temp2 = dt[i-1][rem]
                    temp3 = temp2 + temp
                    dt[i][j] = temp3
                    if(dt[i-1][i-1]>dt[i][j]):
                        dt[i][j] = dt[i-1][j]
                    if(i == len(v)+1):
                        return
                    if j == 5:
                        dp(i+1,0,v,w,vw,dt)
                    else:
                        dp(i,j+1,v,w,vw,dt)

            elif(vw[i] > w[j]):
                temp = dt[i-1][j]
                dt[i][j] = dt[i-1][j]
                if i == len(v)+1:
                        return
                if j == 5:
                    dp(i+1,0,v,w,vw,dt)
                else:
                    dp(i,j+1,v,w,vw,dt)
                    
        except IndexError:
            dp(i+1,0,v,w,vw,dt)
            
            
            
                
                
                
            
            
        
dp(0,0,v,w,vw,dt)
print(dt[len(vw)-1][len(w)-1])
                    

                
                    
               
