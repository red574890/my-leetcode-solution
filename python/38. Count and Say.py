class Solution:
    def countAndSay(self, n: int) -> str:
        
        start = 1
        
        def create_sub(num):
            '''
            num : int
            ---
            return the concept of count and say
            
            '''
            
            num_str = str(num)
            
            same = num_str[0]
            res = []
            tmp_count = 0
            for i in num_str:

                if(i == same):
                    tmp_count+=1
                else:
                    res.append(str(tmp_count))
                    res.append(str(same))
                    same = i
                    tmp_count = 1
            res.append(str(tmp_count))
            res.append(str(same))      
            
            res = ''.join(res)       
            return res

            
        
        def sub_count_say(current,start,end):
            
            if(start == n):
                return str(current)
            else:
                current = create_sub(current)
                return sub_count_say(current,start+1,end)
