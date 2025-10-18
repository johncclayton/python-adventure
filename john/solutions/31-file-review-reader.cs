using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = Console.ReadLine() ?? string.Empty;

        try
        {
            var lines = File.ReadAllLines(path);
            int cheerCount = 0;
            int jeerCount = 0;

            foreach (var line in lines)
            {
                if (line.Contains("cheer", StringComparison.OrdinalIgnoreCase))
                {
                    cheerCount++;
                }
                if (line.Contains("jeer", StringComparison.OrdinalIgnoreCase))
                {
                    jeerCount++;
                }
            }

            Console.WriteLine($"Cheers spotted: {cheerCount}");
            Console.WriteLine($"Jeers spotted: {jeerCount}");
        }
        catch (IOException ex)
        {
            Console.WriteLine($"Reading failed: {ex.Message}");
        }
    }
}
