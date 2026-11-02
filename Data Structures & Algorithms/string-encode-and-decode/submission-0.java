class Solution {

    public String encode(List<String> strs) {
        StringBuilder encoded = new StringBuilder();
        for(String s : strs) {
            encoded.append(s.length()).append('/').append(s);
        }
        return encoded.toString();
    }

    public List<String> decode(String str) {
        List<String> result = new ArrayList<>();
        int i = 0;
        while (i < str.length()) {
            int slash = str.indexOf('/', i);
            int len = Integer.parseInt(str.substring(i, slash));
            result.add(str.substring(slash + 1, slash + 1 + len));
            i = slash + 1 + len;
        }

        return result;
    }
}

