using System;

class Program
{
    static void Main(string[] args)
    {
        int T = int.Parse(Console.ReadLine());

        for (int i = 0; i < T; i++)
        {
            int N = int.Parse(Console.ReadLine());

            bool is_odd = (N % 2 == 1) ? true : false;

            if (is_odd)
            {
                int maximum = N / 2;
                string[] pair = new string[maximum];

                for (int j = 1; j <= maximum; j++)
                {
                    pair[j - 1] = j.ToString() + " " + (N - j).ToString();
                }

                Console.WriteLine("Pairs for " + N.ToString() + ": " + String.Join(", ", pair));
            }

            else
            {
                int maximum = N / 2;
                string[] pair = new string[maximum - 1];
                for (int j = 1; j < maximum; j++)
                {
                    pair[j - 1] = j.ToString() + " " + (N - j).ToString();
                }

                Console.WriteLine("Pairs for " + N.ToString() + ": " + String.Join(", ", pair));
            }

        }
    }
}