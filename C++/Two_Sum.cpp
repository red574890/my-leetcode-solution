class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int>returnVector;
        int b=0;
        for(int i = 0; i < nums.size(); i++){
            for(int j=0; j< nums.size();j++){
                if(i != j){
                    if((nums[i]+nums[j]) == target){
                        returnVector.push_back(i);
                        returnVector.push_back(j);
                        b=1;
                    }
                    if(b==1){break;}
                }
            }
            if(b==1){break;}
        }
        return returnVector;
    }
  
};
