using System;
using System.Text;

class Program
{
    static void Main(string[] args)
    {

        int N = int.Parse(Console.ReadLine());

        StringBuilder sb = new StringBuilder();

        for (int i = 1; i <= N; i++)
        {
            sb.AppendLine(i.ToString());
        }
        string answer = sb.ToString();

        Console.WriteLine(answer);
    }
}