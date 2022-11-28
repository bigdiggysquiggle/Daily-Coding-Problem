import java.util.HashSet;

public class Solution   {
    public static Boolean isValid(String str, Integer k)   {
        //System.out.println("validating: " + str);
        HashSet<Character> test = new HashSet<>();
        for (Character c: str.toCharArray())  {
            test.add(c);
            if (test.size() > k)
                return false;
        }
        return true;
    }
    public static String longestSub(String str, Integer k) {
        if (str.length() == 0)
            return str;
        int start = 0;
        int end = 1;
        String sol = "";
        while (end <= str.length())  {
            //System.out.println("Start " + start + " End " + end + " len " + str.length());
            String tmp = str.substring(start, end);
            if (isValid(tmp, k)) {
                end++;
                if (tmp.length() > sol.length())
                    sol = tmp;
            } else if (start < end) {
                start++;
            }
        }
        return sol;
    }
    public static void test(String str, Integer k)  {
        System.out.println("Test string: \"" + str + "\" k=" + k);
        System.out.println("> " + longestSub(str, k));
    }
    public static void main(String[] args)  {
        test("aabbcc", 2);
        test("aabacbebebe", 3);
        test("aaaaaaaaaaaabcdaaaaaaaaad", 3);
        test("", 4);
    }
}