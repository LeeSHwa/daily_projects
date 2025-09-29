// https://www.acmicpc.net/problem/4892

// 문제 - 숫자 맞추기 게임

using System;

class Program
{
    static void Main(string[] args)
    {
        int count = 1;

        while (true)
        {
            int n0 = int.Parse(Console.ReadLine());

            if (n0 == 0) break; // 0이면 break

            int n1 = n0 * 3;

            bool isOdd = (n1 % 2 == 0) ? false : true;

            int n2 = (n1 % 2 == 0) ? n1 / 2 : (n1 + 1) / 2;

            int n3 = 3 * n2;

            int n4 = n3 / 9;

            Console.WriteLine((isOdd) ? count.ToString() + ". " + "odd " + n4.ToString() : count.ToString() + ". " + "even " + n4.ToString());

            count++;
        }
    }
}