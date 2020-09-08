class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def split(word):
            return [char for char in word]  
        
        temp=split(digits)
        
        phone={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        if(digits==""):
            ret=""
        else:
            res=split(phone[temp[0]])
            ret=[]
            n=1
        
            def combine(temp,phone,res,n):
                res1=[]
                alll=[]
                if(n<len(temp)):
                    now=temp[n]
                    l_o_p=phone[now]
                    for i in range(0,len(res)):
                        for j in range(0,len(l_o_p)):
                            res1.append(res[i]+l_o_p[j])
                    n+=1
                    res=combine(temp,phone,res1,n)
                    return res
                else:
                    return res

        
            ret=combine(temp,phone,res,n)

        return(ret)
