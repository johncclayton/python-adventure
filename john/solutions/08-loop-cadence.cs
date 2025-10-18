using System;

class Program
{
    static void Main()
    {
        int beats = int.Parse(Console.ReadLine() ?? "0");

        for (int i = 0; i < beats; i++)
        {
            Console.WriteLine($"Beat {i + 1}: BOOM");
        }

        Console.WriteLine("Cadence locked in!");
    }
}
