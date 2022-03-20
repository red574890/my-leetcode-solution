class Solution:
    def myAtoi(self, s: str) -> int:
        tmp = s.strip()
        if(len(tmp)==0):
            return 0
        tmp = tmp.split()[0]
        
        
        for i in range(0,len(tmp)):
             if(tmp[len(tmp) - i - 1].isdigit() ):
                    tmp = tmp[0:len(tmp) - i - 1+1]
                    break
                    
        stop = False
        for i in range(len(tmp)):
            if((tmp[i]=="+" or tmp[i] =="-") and i==0):
                continue
    
            if(tmp[i].isdigit() == False):
                stop = True
                break
                
        if(stop):
            tmp = tmp[0:i]  
        else:
            tmp = tmp[0:i+1]
            
        
 
        try:
            tmp = int(float(tmp))
            if(tmp > 2**31 - 1 ):
                return 2**31 - 1
            elif(tmp < -2**31 ):
                return -2**31
            else:
                return tmp
        except:
            return 0
         

        
        
        
