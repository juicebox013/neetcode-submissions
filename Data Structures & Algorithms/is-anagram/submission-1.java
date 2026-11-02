class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) {
            return false;
        }
        //creating an array for each letter in alphabet
        int[] count = new int[26];
        for(int i = 0; i < s.length(); i++) {
            //we are subtracting by 'a' to get the INDEX of each character. If we have the letter 'a' and subtract 'a', we get index 0 etc.     
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }

        for(int val : count) {
            if(val != 0) {
                return false;
            }
        }
        return true;

    }
}