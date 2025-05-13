import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;

public class BOJ9046 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader (System.in));

        int n = Integer.parseInt(br.readLine());


        for (int i = 0; i < n; i ++){
            String temp = br.readLine();
            HashMap<Character, Integer> map = new HashMap<>();

            for (int j = 0; j < temp.length(); j++) {
                char c = temp.charAt(j);
                if (map.getOrDefault(c,0) >= 1){ // 그냥 map.get()으로 비교해버리게 됐을 때, key가 없다면 null을 반환, null 에러 발생
                    map.put(c, map.get(c) + 1);
                }
                else map.put(c, 1);
            }
            System.out.println(map.values());
        }

        



    }
}
