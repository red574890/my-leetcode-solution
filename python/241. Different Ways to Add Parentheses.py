class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
  
       

        def split_char(txt):
            
            if(txt.isdigit()):
                return [int(txt)]

            sub_res = []

            for i in range(len(txt)):
                if txt[i] in "+-*":
   
                    left_list = split_char(txt[0:i])
                    right_list = split_char(txt[i + 1 :])


                    for l in left_list:
                        for r in right_list:
                            if txt[i] == "+":
                                sub_res.append(l + r)
                            elif txt[i] == "-":
                                sub_res.append(l - r)
                            elif txt[i] == "*":
                                sub_res.append(l * r)
        
            return sub_res


        return split_char(expression)
            



