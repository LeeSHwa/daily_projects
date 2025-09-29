using System;

class Program
{
    static void Main(string[] args)
    {
        int antennas = int.Parse(Console.ReadLine());
        int eyes = int.Parse(Console.ReadLine());

        // TroyMartian
        if (antennas >= 3 && eyes <= 4)
        {
            Console.WriteLine("TroyMartian");
        }

        // VladSaturnian
        if (antennas <= 6 && eyes >= 2)
        {
            Console.WriteLine("VladSaturnian");
        }

        // GraemeMercurian
        if (antennas <= 2 && eyes <= 3)
        {
            Console.WriteLine("GraemeMercurian");
        }

    }
}