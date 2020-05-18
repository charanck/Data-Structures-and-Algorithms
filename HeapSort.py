#Heap Sort
class HeapSort:
    
    def __init__(self,li):
        self.list =[0]
        self.out=[]
        for i in li:
            self.list.append(i)
            if(len(self.list) > 3):
                self.reorder(len(self.list)-1)
        while len(self.list)>1:
            self.delmax(1)
        print(self.out)
            
    def reorder(self,i):
        if(i==1):
            return
        if self.list[i//2] < self.list[i]:
            self.list[i//2] , self.list[i] =  self.list[i], self.list[i//2]
            self.reorder(i//2)
        else:
            return
            
    def delmax(self,i):
        if len(self.list) < 3:
            v = self.list[i]
            self.out.append(v)
            self.list.pop(i)
            return
            
        if i*2 < len(self.list):
            self.delmax(i*2)
        else:
            self.list[1],self.list[i]  = self.list[i],self.list[1]
            v = self.list[i]
            self.out.append(v)
            self.list.pop(i)
            self.bubbledown(1)

    def bubbledown(self,i):
        try:
            if(i==1):
                if(self.list[i*2] > self.list[(i*2)+1]):
                    self.list[i*2] , self.list[i] =  self.list[i], self.list[i*2]
                    self.bubbledown(i*2)
                else:
                    self.list[(i*2)+1] , self.list[i] =  self.list[i], self.list[(i*2)+1]
                    self.bubbledown((i*2)+1)
                    
                    
            if(self.list[i*2] >  self.list[i]):
                self.list[i*2] , self.list[i] =  self.list[i], self.list[i*2]
                self.bubbledown(i*2)
                
        except IndexError:
            return
                
            
            
            
hs = HeapSort([1,8,9,5,4,3,6,2,7,10,99])
            
            
            
