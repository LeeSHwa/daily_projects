// https://www.acmicpc.net/problem/10699

// 오늘 날짜

using System;

class Program
{
    static void Main(string[] args)
    {
        DateTime todayDate = DateTime.Today;

        Console.WriteLine(todayDate.ToString("yyyy-MM-dd"));
    }
}