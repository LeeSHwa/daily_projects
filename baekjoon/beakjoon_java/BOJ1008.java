// https://www.acmicpc.net/problem/1008
import java.util.Scanner;

public class BOJ1008 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);

        double[] list = {0, 0};

        list[0] = sc.nextInt();
        list[1] = sc.nextInt();
        double ans = list[0]/list[1];

        sc.close();

        System.out.println(ans);
    }
}