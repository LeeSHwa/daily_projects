// https://www.acmicpc.net/problem/9316

// 문제 - Hello Judge

using System;

class Program
{
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());

        for (int i = 0; i < N; i++)
        {
            Console.WriteLine($"Hello World, Judge {i + 1}!");
        }
    }
}