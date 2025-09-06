class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        current_length = 0
        word_list = []
        n = 0
        while(n<len(words)):
            w = words[n]
      

             
            if(current_length+len(w)<maxWidth):
                word_list.append(w)
                current_length += len(w)+1
                n+=1
            elif(current_length+len(w)==maxWidth):
                word_list.append(w)
                s = " ".join(word_list)
                current_length = 0
                res.append(s)
                word_list = []
                n+=1
            else:
                # rearrange empty space
                total_length = total_length = sum(len(x) for x in word_list)
            
                extra_space = maxWidth-total_length
                if(len(word_list)>1):
                    quotient = extra_space  // (len(word_list)-1)
                    remainder = extra_space % (len(word_list)-1)

                    new_word_list = []

                    for i in range(len(word_list)):
                        if(i<len(word_list)-1):
                            new_word_list.append(word_list[i])
                            if(remainder>0):
                                new_word_list.append(' '*(quotient+1))
                                remainder-=1
                            else:
                                new_word_list.append(' '*(quotient))
                        else:
                            new_word_list.append(word_list[i])
                    
                    s = ''.join(new_word_list)
                else:
                    s = word_list[0]+' '*extra_space
                new_word_list = []
                res.append(s)
                word_list = []
                current_length = 0
        #process what remaining in the word list
        if(len(word_list)>0):
            s = ' '.join(word_list)
            extra = maxWidth-len(s)

            s+=" "*extra
            res.append(s)
 
        return res
                        

                     






