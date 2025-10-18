using System;

enum SwampMood
{
    Chill = 1,
    Snarky = 2,
    Chaotic = 3
}

class Program
{
    static void Main()
    {
        string input = Console.ReadLine() ?? string.Empty;

        if (Enum.TryParse<SwampMood>(input, true, out var mood))
        {
            Console.WriteLine($"Mood logged: {mood} ({(int)mood})");
        }
        else
        {
            var fallback = SwampMood.Chaotic;
            Console.WriteLine($"Mood unreadable, defaulting to {fallback} ({(int)fallback})");
        }
    }
}
