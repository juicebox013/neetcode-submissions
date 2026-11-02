class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> index = new HashMap<>();
        int left = 0;
        int right = nums.length - 1;
        int complement = 0;
        for(int i = 0; i < nums.length; i++) {
            int num = nums[i];
            complement = target - num;
            if(index.containsKey(complement)) {
                return new int [] {index.get(complement), i};
            }
            index.put(num, i);
        }
        return new int[] {};

    }
}
