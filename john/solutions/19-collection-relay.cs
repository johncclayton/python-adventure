using System;

class Program
{
    static void Main()
    {
        int[] relay = new int[3];
        int total = 0;

        for (int i = 0; i < relay.Length; i++)
        {
            relay[i] = int.Parse(Console.ReadLine() ?? "0");
            total += relay[i];
        }

        for (int i = 0; i < relay.Length; i++)
        {
            Console.WriteLine($"Runner {i + 1}: {relay[i]} minutes");
        }

        Console.WriteLine($"Total torch time: {total}");
    }
}
