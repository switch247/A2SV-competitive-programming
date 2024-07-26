class Solution {
  List<int> twoSum(List<int> nums, int target) {
    List<int>? ans = [];
    for (var i = 0; i < nums.length-1; i++){
        for (var j =i+1; j< nums.length; j++){
            if (nums[i]+nums[j]== target){
                ans.add(i);
                ans.add(j);
            }
            }
    }
    return ans;

  }
}