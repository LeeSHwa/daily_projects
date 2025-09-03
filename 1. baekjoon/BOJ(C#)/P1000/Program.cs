using System;
using System.Linq; // Split().Select() 등을 사용하기 위해 필요

class Program
{
    static void Main(string[] args)
    {
        // 한 줄을 읽어옴. 예: "1 5"
        string input = Console.ReadLine();

        // 공백을 기준으로 문자열을 나눔. 예: ["1", "5"]
        string[] numbers = input.Split(' ');

        // 각 문자열을 정수(int)로 변환
        int A = int.Parse(numbers[0]);
        int B = int.Parse(numbers[1]);
        
        // 두 숫자의 합을 출력
        Console.WriteLine(A + B);
    }
}