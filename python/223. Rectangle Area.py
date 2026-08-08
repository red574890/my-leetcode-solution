class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        overlapping = False
        right_x = max(ax2,bx2)
        left_x  = min(ax1,bx1)
        top_y = max(ay2,by2)
        down_y = min(ay1,by1) 
        if((abs(right_x-left_x) < (abs(ax2-ax1)+abs(bx2-bx1))) and (abs(top_y-down_y) < (abs(ay2-ay1)+abs(by2-by1)))  ):
            overlapping = True
         
        

        if(overlapping):
            left_point_x = max(ax1,bx1) 
            left_point_y = max(ay1,by1) 

            right_point_x = min(ax2,bx2) 
            right_point_y = min(ay2,by2)


            tmp = abs(left_point_x -right_point_x ) * abs(left_point_y -right_point_y)
            print(tmp)
            return (abs(ax2-ax1)*abs(ay1-ay2)) +  (abs(bx2-bx1)*abs(by2-by1)) - tmp

        else:
   

            return (abs(ax2-ax1)*abs(ay1-ay2) +  abs(bx2-bx1)*abs(by2-by1)) 




