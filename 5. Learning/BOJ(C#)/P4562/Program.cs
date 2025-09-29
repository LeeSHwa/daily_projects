// https://www.acmicpc.net/problem/4562

// 문제 - No Brainer

using System;

class Program
{
    static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine());

        for (int i = 0; i < n; i++)
        {
            string[] str_inputs = Console.ReadLine().Split();
            int[] numbers = Array.ConvertAll(str_inputs, int.Parse);

            Console.WriteLine((numbers[0] >= numbers[1]) ? "MMM BRAINS" : "NO BRAINS");

            // if (numbers[0] >= numbers[1]){
            // {
            //     Console.WriteLine("MMM BRAINS");
            // }

            // else
            // {
            //     Console.WriteLine("NO BRAINS");
            // }
        }
    }
}