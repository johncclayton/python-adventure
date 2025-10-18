using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        var assignments = new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase)
        {
            ["Undersea Dome"] = "Mimic Chest",
            ["Labyrinth Hub"] = "Bard",
            ["Swamp Lounge"] = "Barbarian"
        };

        string room = Console.ReadLine() ?? string.Empty;
        if (assignments.TryGetValue(room, out string? guardian))
        {
            Console.WriteLine($"Guardian on duty: {guardian}");
        }
        else
        {
            Console.WriteLine("No guardian scheduled. Summon the intern.");
        }

        foreach (var entry in assignments.OrderBy(kvp => kvp.Key, StringComparer.Ordinal))
        {
            Console.WriteLine($"{entry.Key} -> {entry.Value}");
        }
    }
}
