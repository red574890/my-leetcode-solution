class Solution {
public:
    int divide(int dividend, int divisor) {
        int ds=1;
        int dd=1;
        int av=1;//addvalue
        if(divisor==1 ){
            return dividend;
        }else if(divisor==-1){
            if(dividend<0){
                if(dividend<=-2147483648){return 2147483647;}
                else{return -dividend;}
            }else{
                if(dividend>=2147483648){return -2147483647;}
                else{return -dividend;}
            }
        }else{
            int dis=0;
              int i=0;
              int change=0;
              int change1=0;
              if( divisor<0){
                  ds=-1;
                  if(divisor<=-2147483648){divisor = 2147483647; change1=1;}
                  else{divisor=-divisor;}
                  
              }else{
                  if(divisor>=2147483648){divisor = 2147483647;}
              
              }
            
            
              if(dividend<0){
                  dd=-1;
                  if(dividend<=-2147483648){
                      dividend=2147483647;
                      change=1;
              
                      
                  }else{
                      dividend=-dividend;
                  }
                  
              }else{
                  if(dividend>=2147483648){
                      dividend=2147483647;
                      change=1;
              
                  }
              }
              
              if(ds+dd==0){
                  av=-1;
              }
            if(dividend<divisor){
                return 0;
            }
            
  
            if(change1==1 && change==0){
                return 0;
            }
            
            
              int t=1;
              double cdivisor=divisor;
      
              while(dividend>0 && (dividend>=divisor)){
                  t=1;
                  dividend-=cdivisor;
                  if(change==1){
                      dividend+=1;
                      change=0;
                  }
                  dis+=av;
                 
                  while((t+t)*cdivisor<=dividend ){
                      t+=t;
                      dis+=t*av;
                      dividend-=t*cdivisor;
                      if(t>=536870912){
                          break;
                      }
            
                  }
                 
        
                  
                  
                  //if(dividend-i<divisor){break;}
           
               }
              return dis;
       
        
        
    }
}
};
