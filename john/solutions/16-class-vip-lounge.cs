using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var checklist = new LoungeChecklist(new[] { "Bard", "Mimic Chest" });
        string name = Console.ReadLine() ?? string.Empty;

        Console.WriteLine(checklist.Describe());
        if (checklist.CanEnter(name))
        {
            Console.WriteLine($"Welcome {name}!");
        }
        else
        {
            Console.WriteLine($"Sorry {name}.");
        }
    }
}

internal class LoungeChecklist
{
    private readonly HashSet<string> _allowed;

    public LoungeChecklist(IEnumerable<string> names)
    {
        _allowed = new HashSet<string>(names, StringComparer.OrdinalIgnoreCase);
    }

    public bool CanEnter(string name)
    {
        return _allowed.Contains(name ?? string.Empty);
    }

    public string Describe()
    {
        return $"VIPs: {string.Join(", ", _allowed)}";
    }
}
