class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> table = new HashSet<>();
        for(int num : nums) {
            if(table.contains(num)) {
                return true;
            }
            table.add(num);
        }
        return false;
    }
}