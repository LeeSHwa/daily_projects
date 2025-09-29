// https://www.acmicpc.net/problem/7891

// 문제 - Can you add this?
using System;
using System.Linq;

class Program
{
    static void Main(string[] args)
    {
        int t = int.Parse(Console.ReadLine());

        for (int i = 0; i < t; i++)
        {
            int[] numbers = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();

            Console.WriteLine(numbers[0] + numbers[1]);
        }
    }
}