class Solution {
  List<int> twoSum(List<int> nums, int target) {
    List<int>? ans = [];
    Map<int,dynamic> test = {};
    for (var i = 0; i < nums.length; i++){
        var x = target - nums[i];
        if (test.containsKey(nums[i])){
            ans.add(i);
            ans.add(test[nums[i]]);
        }
         test[x] = i;

    }
    return ans;

  }
}