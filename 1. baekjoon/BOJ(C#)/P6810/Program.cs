// https://www.acmicpc.net/problem/6810

// ISBN

using System;
using System.Collections;

class Program
{
    static void Main(string[] args)
    {
        List<int> numbers = new List<int> { 9, 7, 8, 0, 9, 2, 1, 4, 1, 8 };

        for (int i = 0; i < 3; i++)
        {
            int num = int.Parse(Console.ReadLine());
            numbers.Add(num);
        }

        int sum = 0;

        for (int j = 0; j < numbers.Count; j++)
        {
            if (j % 2 == 0)
            {
                sum += numbers[j];
            }

            else
            {
                sum += numbers[j] * 3;
            }
        }

        Console.WriteLine($"The 1-3-sum is {sum}");
    }
}