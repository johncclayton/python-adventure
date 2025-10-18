using System;
using System.Linq;

class Program
{
    static void Main()
    {
        string[] jokes =
        {
            "The maze has better signals than my phone.",
            "Mud taxes are the pits.",
            "Maze maintenance is just wall hugging.",
            "Undersea stand-ups are bubbles of joy."
        };

        var approved = jokes
            .Where(j => j.Contains("maze", StringComparison.OrdinalIgnoreCase) && j.Length < 40)
            .Select(j => $"Approved: {j}")
            .ToList();

        foreach (var joke in approved)
        {
            Console.WriteLine(joke);
        }

        Console.WriteLine($"Total approved: {approved.Count}");
    }
}
