//The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
//
//dir
//    subdir1
//        file1.ext
//        subsubdir1
//    subdir2
//        subsubdir2
//            file2.ext

import java.util.Arrays;

public class Solution23 {
    public static int longest(String[] set, int depth)  {
        int len = set[0].length();
        int longest = 0;
        System.out.println("Depth: " + depth);
        for (int i = 1; i < set.length; i++)    {
            int count = 0;
            int tmp = 0;
            while (set[i].charAt(count) == '\t')
                count++;
            System.out.println("Count: " + count + set[i]);
            if (count < depth)
                break;
            else if (count > depth)
                tmp = longest(Arrays.copyOfRange(set, i, set.length), depth + 1);
            tmp += set[i].length() - count;
            System.out.println("tmp: " + tmp + set[i]);
            if (tmp > longest)
                longest = tmp;
        }
        return len + longest;
    }
    public static void main(String[] args)  {
        System.out.println("Expecting 32");
        System.out.println(longest("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext".split("\n"), 0));
    }
}