using System;
using System.Collections.Generic;
using System.Text.Json;

class Program
{
    static void Main()
    {
        string jsonInput = Console.ReadLine() ?? "[]";

        var guardians = JsonSerializer.Deserialize<List<Guardian>>(jsonInput) ?? new List<Guardian>();

        foreach (var guardian in guardians)
        {
            Console.WriteLine($"Arrival: {guardian.Name} - {guardian.Role} - Glowsticks {guardian.GlowstickCount}");
        }

        var glowing = guardians.FindAll(guardian => guardian.GlowstickCount > 0);
        Console.WriteLine("Manifest:");
        string manifest = JsonSerializer.Serialize(glowing, new JsonSerializerOptions { WriteIndented = true });
        Console.WriteLine(manifest);
    }
}

class Guardian
{
    public string Name { get; set; } = string.Empty;
    public string Role { get; set; } = string.Empty;
    public int GlowstickCount { get; set; }
}
