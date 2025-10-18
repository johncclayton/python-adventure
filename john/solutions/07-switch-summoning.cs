using System;

class Program
{
    static void Main()
    {
        string input = Console.ReadLine() ?? string.Empty;
        var parts = input.Split(',', 2, StringSplitOptions.TrimEntries);
        string artifactName = parts.Length > 0 ? parts[0] : string.Empty;
        int riskLevel = parts.Length > 1 && int.TryParse(parts[1], out int parsed) ? parsed : 0;

        string handler = (artifactName, riskLevel) switch
        {
            var (name, level) when name.Contains("Lantern", StringComparison.OrdinalIgnoreCase) && level < 5 => "Router Bard",
            var (name, _) when name.Contains("Mud", StringComparison.OrdinalIgnoreCase) => "Barbarian Curator",
            var (name, _) when name.Contains("Scroll", StringComparison.OrdinalIgnoreCase) => "Archivist Eel",
            _ => "Intern Gargoyle"
        };

        Console.WriteLine($"Handler assigned: {handler}");
    }
}
