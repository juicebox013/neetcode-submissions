class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> frequency = new HashMap<>();
        int[] result = new int[k];
        for(int num : nums) {
            frequency.put(num, frequency.getOrDefault(num, 0) + 1);
        }
        for(int i = 0; i < k; i++) {
            //put the variables here so they reset every loop
            int maxFreq = 0;
            int mostFreq = 0;
            for(int key : frequency.keySet()) {
                int count = frequency.get(key);
                if(count > maxFreq) {
                    maxFreq = count;
                    mostFreq = key;
                }
            }
            result[i] = mostFreq;
            frequency.remove(mostFreq);
        }
        return result;
    
    }
}
