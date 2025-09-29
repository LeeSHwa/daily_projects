package Solved;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class BOJ11720 {
    public static void main(String[] args) throws Exception {
        // Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader (System.in));
        
        int n = Integer.parseInt(br.readLine());
        int hap = 0;
        
        String num = br.readLine();

        // char[] numList = num.toCharArray();
        

        if (num.length() == n){
            for (int i = 0; i < num.length(); i ++){
                hap += num.charAt(i) - '0';
            }

            System.out.println(hap);
        }
        else throw new Exception();

    }
    
}
