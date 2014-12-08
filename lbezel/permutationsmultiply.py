class permutation:
        
        def __init__(self, wb):
            self.wb = wb

                
        def __mul__(self, b):
           ab = permutation({}) 
           for i in b.wb.keys():
                        for j in self.wb.keys():
                                if b.wb[i] == j:
                                        ab.wb[i] = self.wb[j]            
           return(ab.wb)      
        def __str__(self):

           return(str(self.wb))
  
a1 = permutation({1:4, 2:5, 3:1, 4:3, 5:2})
b1 = permutation({1:2, 2:3, 3:4, 4:5, 5:1})
a1b1 = a1*b1
b1a1 = b1*a1
print(a1b1, b1a1)
