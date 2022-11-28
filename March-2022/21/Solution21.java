import java.util.Random;

public class Solution21 {
    public static Random rng = new Random(System.currentTimeMillis());
    static Integer count = 0;
    static Integer choice = 0;
    public static Integer selRand(int x)    {
        count++;
        if (count == 1)
            choice = x;
        else {
            int i = rng.nextInt(count);
            System.out.println(i + "==" + (count - 1));
            if (i == count - 1)
                choice = x;
        }
        return choice;
    }
    public static void main(String[] args)  {
        Integer[] ar = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        for (int i = 0; i < 10; i++)
            ar[i] = rng.nextInt();
        System.out.print("{ " + ar[0]);
        for (int i = 1; i < 10; i++)
            System.out.print(", " + ar[i]);
        System.out.println(" }");
        for (int i = 0; i < 10; i++)
            System.out.println("Choice " + i + " from stream: " + selRand(ar[i]));
    }
}