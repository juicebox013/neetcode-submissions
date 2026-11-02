class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<HashMap<Character, Integer>, List<String>> groups = new HashMap<>();
        for(String s : strs) {
           HashMap<Character, Integer> word = new HashMap<>();
           for(int i = 0; i < s.length(); i++) {
            word.put(s.charAt(i), word.getOrDefault(s.charAt(i), 0) + 1);
           }
           if(!groups.containsKey(word)) {
            groups.put(word, new ArrayList<>());
           }
           groups.get(word).add(s);
        }
        return new ArrayList<>(groups.values());
    }
}
