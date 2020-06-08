letters=['a','b','c','d','e','f']
final = []

def combinations(values,loc):
    if loc == 1:
        print(values)
        return
    global final
    for i in range(len(values)):
        start=values[i]
        k=values[:]
        k.remove(start)
        _combinations(loc,start,k,[start])
    for y in final:
        print(y)
    
def _combinations(l,start,rem,cur):
    global final
    if len(cur) == l:
        cur = sorted(cur)
        if cur in final:
            return
        else:
            final.append(cur)
    else:
        for i in range(len(rem)):
            s = rem[i]
            x=rem[:]
            x.remove(s)
            n =cur + [s]
            _combinations(l,s,x,n)
            
combinations(letters,3)
