using System;
using System.IO;

class Program
{
    static void Main()
    {
        string sourcePath = Console.ReadLine() ?? string.Empty;
        string destinationPath = Console.ReadLine() ?? string.Empty;

        using var reader = new StreamReader(sourcePath);
        using var writer = new StreamWriter(destinationPath, append: false);

        while (!reader.EndOfStream)
        {
            string? line = reader.ReadLine();
            if (line is null)
            {
                continue;
            }

            writer.WriteLine($"Grateful note: {line}");
        }

        Console.WriteLine("Copy complete.");
    }
}
