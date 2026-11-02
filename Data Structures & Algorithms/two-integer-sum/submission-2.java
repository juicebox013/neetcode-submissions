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
                // we put the complemented number first because we are checking if the complement
                //, or the number required to make the target value, has already been seen. in other 
                //words, it would be of the lower index, therefore placing it first.
                ans[0] = index.get(complement);
                ans[1] = i;
                return ans;
            }
            index.put(num, i);
        }
        return new int[] {};

    }
}
