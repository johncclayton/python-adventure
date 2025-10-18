using System;

class Program
{
    static void Main()
    {
        int torchCount = int.Parse(Console.ReadLine() ?? "0");
        bool bootsAreWaterproof = bool.Parse(Console.ReadLine() ?? "false");
        int mudForecast = int.Parse(Console.ReadLine() ?? "0");

        bool entryGranted = torchCount >= 2 && bootsAreWaterproof && mudForecast < 7;

        Console.WriteLine(entryGranted ? "Entry granted!" : "Entry denied!");

        if (!entryGranted && mudForecast < 4)
        {
            Console.WriteLine("Grab extra towels before reapplying.");
        }
    }
}
