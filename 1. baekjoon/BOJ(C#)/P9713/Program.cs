using System;

class Program
{
    static void Main(string[] args)
    {
        int T = int.Parse(Console.ReadLine());

        for (int i = 0; i < T; i++)
        {
            int sum = 0;

            int number = int.Parse(Console.ReadLine());
            for (int j = 1; j <= number; j += 2)
            {
                sum += j;
            }

            Console.WriteLine(sum);
            }
        }
    }