import java.util.Random;

public class Solution20   {
    public static void solve(Integer iter)   {
        Random rng = new Random(System.currentTimeMillis());
        int sq_p = 0;
        int c_p = 0;
        for (int i = 0; i < iter; i++)  {
            float x = rng.nextFloat();
            float y = rng.nextFloat();
//            System.out.println(x + " " + y);
            if ((x*x) + (y*y) <= 1)
                c_p++;
            sq_p++;
//            System.out.println("Points " + c_p + " " + sq_p);
        }
//        System.out.println("Floats" + (float)c_p/sq_p);
        System.out.printf("Pi is approx %.3f\n",(float)4 * ((float)c_p/sq_p));
    }
    public static void test(Integer iter)   {
        System.out.println("Testing for " + iter + " iterations");
        solve(iter);
    }
    public static void main(String[] args)  {
        test(10);
        test(100);
        test(1000);
    }
}
