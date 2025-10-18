using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var plannedPepTalks = new List<string>();
        string? line;

        while (!string.IsNullOrEmpty(line = Console.ReadLine()))
        {
            plannedPepTalks.AddRange(GetAssignments(line));
        }

        foreach (var entry in plannedPepTalks)
        {
            Console.WriteLine(entry);
        }
    }

    private static IEnumerable<string> GetAssignments(string biome)
    {
        var assignments = new List<string>();
        var companion = ChooseCompanion(biome, out var reason);
        assignments.Add($"{biome.ToUpperInvariant()} -> {companion} ({reason})");

        if (biome.Contains("mud", StringComparison.OrdinalIgnoreCase))
        {
            assignments.Add($"{biome.ToUpperInvariant()} -> Mimic Chest (backup pep talk, excessive echo)");
        }

        return assignments;
    }

    private static string ChooseCompanion(string biome, out string reason)
    {
        if (biome.Contains("Labyrinth", StringComparison.OrdinalIgnoreCase))
        {
            reason = "improvise a router-stabilizing ballad";
            return "Bard";
        }

        if (biome.Contains("Swamp", StringComparison.OrdinalIgnoreCase))
        {
            reason = "threaten the mud with pivot tables";
            return "Barbarian";
        }

        if (biome.Contains("Undersea", StringComparison.OrdinalIgnoreCase) ||
            biome.Contains("Sea", StringComparison.OrdinalIgnoreCase))
        {
            reason = "schedule the bubbles and minute the minutes";
            return "Mimic Chest";
        }

        reason = "insist the spotlight is literally a torch";
        return "Bard";
    }
}
