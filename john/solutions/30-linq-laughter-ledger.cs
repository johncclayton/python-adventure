using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        var sessions = new List<(string Room, int Laughs)>
        {
            ("Labyrinth Arena", 18),
            ("Labyrinth Arena", 24),
            ("Swamp Lounge", 14),
            ("Swamp Lounge", 17),
            ("Undersea Dome", 18)
        };

        var grouped = sessions
            .GroupBy(entry => entry.Room)
            .Select(group => new
            {
                Room = group.Key,
                TotalLaughs = group.Sum(entry => entry.Laughs)
            })
            .OrderByDescending(result => result.TotalLaughs)
            .ToList();

        foreach (var result in grouped)
        {
            Console.WriteLine($"{result.Room} -> {result.TotalLaughs} laughs");
        }

        int grandTotal = grouped.Sum(result => result.TotalLaughs);
        Console.WriteLine($"Grand total: {grandTotal}");
    }
}
