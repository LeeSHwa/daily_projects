// https://www.acmicpc.net/problem/8370

// Plane

using System;
using System.Linq;

class Program
{
    static void Main(string[] args)
    {
        int[] line = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();

        Console.WriteLine(line[0] * line[1] + line[2] * line[3]);
    }
}