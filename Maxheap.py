#Here use formula n*2 to get an elements left child and (n*2) + 1 to get its right child

class MaxHeap:
    
    def __init__(self):
        self.list = [0]
        self.size = 0
        
    def add(self,value):
        self.list.append(value)
        self.size += 1
        if len(self.list) > 1:
            self._bubbleup(self.list,value,(len(self.list)-1))
        else:
            return
        
    def print(self):
        print (self.list)
        
        
    def _bubbleup(self,list,value,i):
        if i ==1:
            return
        if value > list[(i//2)]:
            list[i//2],  list[i] = list[i], list[i//2]
            return self._bubbleup(list,value,(i//2))
        else:
            return
        
    def delmax(self):
        if (len(self.list)-1) < 3:
            self.list.pop(1)
        else:
            self._delmax(1)
            
    def _delmax(self,i):
        if (i > (len(self.list)-1)):
            return
        else:
            if(i*2<(len(self.list)-1)):
                self._delmax(i*2)
            else:
                self.list[1] , self.list[i] = self.list[i], self.list[1]
                self.list.pop(i)
                self._bubbledown(1)
                
    def _bubbledown(self,i):
        if i*2 >len(self.list):
            return
        try:
            if self.list[i*2] > self.list[(i*2)+1]:
                self.list[i*2], self.list[i] = self.list[i],  self.list[i*2]
                self._bubbledown(i*2)
            else:
                self.list[(i*2)+1], self.list[i] = self.list[i], self.list[(i*2)+1]
                self._bubbledown(i*2)
        except IndexError:
            self.list[i*2], self.list[i] = self.list[i],  self.list[i*2]
            return
            
            
        
        

        

                
        
        
            
        
        
        
        
bh = MaxHeap()
bh.add(1)
bh.add(10)
bh.add(2)
bh.add(12)
bh.add(22)
bh.add(14)
bh.add(60)
bh.add(80)
bh.add(90)
bh.add(92)
bh.add(72)
bh.add(76)
bh.add(78)
bh.add(53)
bh.add(61)
bh.add(29)
bh.delmax()
bh.delmax()









bh.print()

        
    
        
    
        
