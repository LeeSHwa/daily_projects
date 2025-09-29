// https://www.acmicpc.net/problem/4101

// 문제 - 크냐?

using System;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        bool flag = false;

        while (!flag)
        {
            string[] stringInputs = Console.ReadLine().Split();

            int[] numbers = Array.ConvertAll(stringInputs, int.Parse);

            if (numbers[0] == 0 && numbers[1] == 0)
            {
                flag = true;
            }

            else if (numbers[0] > numbers[1])
            {
                Console.WriteLine("Yes");
            }

            else
            {
                Console.WriteLine("No");
            }
        }
    }
}