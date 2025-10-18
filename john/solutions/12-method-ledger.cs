using System;

class Program
{
    static void Main()
    {
        int torches = 3;
        string mudRating = Console.ReadLine() ?? string.Empty;

        BoostTorch(ref torches);
        bool success = TryInterpretMud(mudRating, out int level);

        Console.WriteLine($"Torches ready: {torches}");
        if (success)
        {
            Console.WriteLine($"Mud level interpreted: {level}");
        }
        else
        {
            Console.WriteLine("Mud level unreadable.");
        }
    }

    private static void BoostTorch(ref int torchCount)
    {
        torchCount += 2;
    }

    private static bool TryInterpretMud(string value, out int level)
    {
        if (int.TryParse(value, out int parsed) && parsed >= 0 && parsed <= 10)
        {
            level = parsed;
            return true;
        }

        level = 0;
        return false;
    }
}
