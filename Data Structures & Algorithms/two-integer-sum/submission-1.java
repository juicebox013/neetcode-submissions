class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> index = new HashMap<>();
        int left = 0;
        int right = nums.length - 1;
        int complement = 0;
        int ans[] = new int[2];
        for(int i = 0; i < nums.length; i++) {
            int num = nums[i];
            complement = target - num;
            if(index.containsKey(complement)) {
                ans[0] = index.get(complement);
                ans[1] = i;
                return ans;
            }
            index.put(num, i);
        }
        return new int[] {};

    }
}
