using System;

class Program
{
    static void Main(string[] args)
    {
        string input = Console.ReadLine();

        int x = Convert.ToInt32(input, 16);

        Console.WriteLine(x);

    }
}