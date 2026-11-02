class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) {
            return false;
        }
        int[] count = new int[26];
        for(int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }

        for(int val : count) {
            if(val != 0) {
                return false;
            }
        }
        return true;

        /*
        hashmap implementation:
        let s = cat;
        let t = tac;

        if (s.length() != t.length()) {
            return false;
        }
        //hashmap stores information using key-value pairs --> in this case, the character in the string
        //is the key, and the integer is the value, which is how many times it appears.

        HashMap<Character, Integer> countS = new HashMap<>();
        HashMap<Character, Integer> countT = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            //s.charAt(i) returns the character at this specific index of the string. --> s.chaAt(0)='c'
            //countS.getOrDefault --> cecks if the key exists in the map
            // 0 is the default value, because if nothing is there, the count is 0
            countS.put(s.charAt(i), countS.getOrDefault(s.charAt(i), 0) + 1);
            countT.put(t.charAt(i), countT.getOrDefault(t.charAt(i), 0) + 1);
        }

        return countS.equals(countT);
        
        */

    }
}
