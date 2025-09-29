// https://www.acmicpc.net/problem/2752

// 세 수 정렬

using System;
using System.Collections.Generic;
class Program
{
    static void Main(string[] args)
    {
        string input = Console.ReadLine();

        string[] numbers = input.Split();

        int a = int.Parse(numbers[0]);
        int b = int.Parse(numbers[1]);
        int c = int.Parse(numbers[2]);

        List<int> list_num = new List<int> { a, b, c };
        list_num.Sort();
        
        Console.WriteLine(string.Join(" ", list_num));
    }
}