class Solution {
public:
    double myPow(double x, int n) {
        //check the sign of n
        int sign=0;
        
        if(x!=1.0 && x!=-1.0){
            if(n>0){
                sign=1;
           }else if(n<0){
                sign=-1;
           }

           double con=1;

 
           if(sign==1 and x!=1 ){
               while(n!=1){
                    if(n%2==1){
                      con*=x;
              
                      n-=1;
                    }
                    n=n/2;
                    x=x*x;
                   cout<<x;
                   
                }
               x=x*con;
            
         
            
          }else if(sign==-1 and x!=1){
               x=(1/x);
               cout<<x;
               while(n!=-1){
                    if(n%2==-1){
                      con*=x;
                      n+=1;
                    }
                    n=n/2;
                    x=x*x;
                   
                }
               x=x*con;
               if(x<0){
                   x=x*-1;
               }
               
            }else if(sign==0 and x!=1){
                   x=1;
               }
            
        }else if(x==1){
                x=1;
        }else if(x==-1){

            if(n&1){
                x=-1;
            }else{
                x=1;
            }
        }
        return x;
    
}
    };
