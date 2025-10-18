using System;
using System.Collections.Generic;

[Flags]
enum GuardianTraits
{
    None = 0,
    Musical = 1,
    Waterproof = 2,
    Glow = 4
}

class Program
{
    static void Main()
    {
        var guardianTraits = new Dictionary<string, GuardianTraits>(StringComparer.OrdinalIgnoreCase)
        {
            ["Bard"] = GuardianTraits.Musical | GuardianTraits.Glow,
            ["Barbarian"] = GuardianTraits.Waterproof,
            ["Mimic Chest"] = GuardianTraits.Glow | GuardianTraits.Waterproof
        };

        string guardian = Console.ReadLine() ?? string.Empty;
        if (guardianTraits.TryGetValue(guardian, out var traits))
        {
            var description = traits == GuardianTraits.None ? "None" : traits.ToString();
            Console.WriteLine($"Traits: {description}");
            Console.WriteLine($"Waterproof? {(traits.HasFlag(GuardianTraits.Waterproof) ? "Yes" : "No")}");
        }
        else
        {
            Console.WriteLine("Guardian not found in roster.");
        }
    }
}
