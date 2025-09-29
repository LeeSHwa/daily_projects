using System;
using System.Linq;

class Program
{
    static void Main(String[] args)
    {
        string input = Console.ReadLine(); // 형 선언은 필수적

        string[] numbers = input.Split(' '); // 리스트의 경우 형 뒤에 붙이네?

        int A = int.Parse(numbers[0]);
        int B = int.Parse(numbers[1]);

        Console.WriteLine(A - B);
    }
}   