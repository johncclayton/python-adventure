using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        var moraleScores = new List<int>();

        while (true)
        {
            string? line = Console.ReadLine();
            if (string.IsNullOrWhiteSpace(line))
            {
                break;
            }

            if (int.TryParse(line, out int score))
            {
                moraleScores.Add(score);
            }
        }

        moraleScores.RemoveAll(score => score < 3);

        for (int i = 0; i < moraleScores.Count; i++)
        {
            Console.WriteLine($"Slot {i}: {moraleScores[i]}");
        }

        double average = moraleScores.Count > 0 ? moraleScores.Average() : 0.0;
        Console.WriteLine($"Average morale: {Math.Round(average, 1, MidpointRounding.AwayFromZero)}");
    }
}
