using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        var snacks = new List<(string Name, int Calories)>
        {
            ("Glow Popcorn", 90),
            ("Mud Pie Bites", 220),
            ("Eel Jerky", 140)
        };

        var cards = snacks
            .Select(snack => new
            {
                snack.Name,
                snack.Calories,
                Mood = snack.Calories < 150 ? "Featherlight" : "Hearty"
            })
            .OrderBy(card => card.Calories);

        foreach (var card in cards)
        {
            Console.WriteLine($"{card.Name}: {card.Mood} ({card.Calories})");
        }
    }
}
