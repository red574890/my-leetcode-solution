class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        def Special_append(a,ele):

            if(len(a[len(a)-1])<2):
                a[len(a)-1].append(ele)
            else:
                a.append([ele])

        def in_interval(ele0,ele1):
            if(a[0]<ele and a[1]>ele):
                return True
            else:
                return False

        if(len(intervals)==0):
            return [newInterval]

        if(intervals[0][0] > newInterval[1]):
            intervals.insert(0, newInterval)
            return intervals

        res = [[]]
        f_found = False
        s_found = False
    
        for i in range(len(intervals)):
            if(intervals[i][0] <= newInterval[0] and intervals[i][1] >= newInterval[1]):
                Special_append(res,intervals[i][0])
                Special_append(res,intervals[i][1])
                f_found = True
                s_found = True
                continue


            if(i+1 < len(intervals)):
                
                if(intervals[i][1]<newInterval[0] and intervals[i+1][0]>newInterval[1]):
                    print('h')
                    Special_append(res,intervals[i][0])
                    Special_append(res,intervals[i][1])
                    Special_append(res,newInterval[0])
                    Special_append(res,newInterval[1])
                    f_found = True
                    s_found = True
                    continue

            for j in range(2):
                if(intervals[i][j] < newInterval[0]):
                    Special_append(res,intervals[i][j])
                elif(intervals[i][j] >= newInterval[0] and f_found == False):
                    f_found = True
                    if(j == 0):
                        Special_append(res,newInterval[0])
          
                elif(intervals[i][j] > newInterval[1] and s_found == False):
                    s_found = True
        
                    if(j == 0):
                        Special_append(res,newInterval[1])
                        Special_append(res,intervals[i][j])
                    elif(j == 1):
                        Special_append(res,intervals[i][j])

                elif(intervals[i][j]>newInterval[1] and s_found):
                    Special_append(res,intervals[i][j])


        
        if(s_found == False and f_found):
            Special_append(res,newInterval[1])
        
        elif(s_found == False and f_found== False):
            Special_append(res,newInterval[0])
            Special_append(res,newInterval[1])

        return res
