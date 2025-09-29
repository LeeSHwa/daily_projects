package Solved;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BOJ9046 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader (System.in));

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i ++){
            String temp = br.readLine(); // 문장을 받을 String 변수
            HashMap<Character, Integer> map = new HashMap<>(); // String의 각 char 부분을 hashmap으로 받아서 카운트
            List<Character> result = new ArrayList<>(); // 이후 value 값들을 비교해서 가장 큰 value들의 key만 모아 둘 array

            // 1. 알파벳 빈도수 계산
            for (int j = 0; j < temp.length(); j++) { 
                char c = temp.charAt(j); // 이터레이션마다 순서에 맞게 글자를 가져옴
                if (Character.isLetter(c)) { // 그 글자가 알파벳이라면
                    map.put(c, map.getOrDefault(c,0) + 1);} // 그 글자를 키 값으로 하는 hashmap의 value를 +1 해줌
            }

            // 2. 최빈값 처리
            int max = Collections.max(map.values()); // value들 중 가장 큰 값을 구하고
            for (Map.Entry<Character, Integer> entry : map.entrySet()) { // map의 entryset을 통해 key, value 값을 가져오고
                if (entry.getValue() == max) { // 만약 value 값이 max와 일치하다면
                    result.add(entry.getKey()); // arraylist에 해당 key값만 추가
                }
            }
            
            // 3. 결과 출력
            if(result.size() == 1) { // 만약 key값을 모아둔 array의 크기가 1이라면
                System.out.println(result.get(0)); // 중복이 없기때문에 해당 key값을 출력
            }
            else {
                System.out.println("?"); // 중복이 있다면 ? 출력
            }            
        }
    }
}
