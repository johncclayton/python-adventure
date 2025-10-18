using System;

class Program
{
    static void Main()
    {
        int validCount = 0;

        while (true)
        {
            string? line = Console.ReadLine();
            if (line is null)
            {
                break;
            }

            string trimmed = line.Trim();
            if (trimmed.Equals("done", StringComparison.OrdinalIgnoreCase))
            {
                break;
            }

            if (int.TryParse(trimmed, out _))
            {
                validCount++;
            }
            else if (!string.IsNullOrEmpty(trimmed))
            {
                Console.WriteLine($"Ignored: {trimmed} croaked");
            }
        }

        Console.WriteLine($"Valid readings: {validCount}");
    }
}
