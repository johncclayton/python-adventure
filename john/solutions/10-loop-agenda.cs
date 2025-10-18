using System;

class Program
{
    static void Main()
    {
        string[] topics =
        {
            "Torches",
            "Snacks",
            "Exit Strategies"
        };

        foreach (var topic in topics)
        {
            string tagline = topic switch
            {
                "Torches" => "infused with glowfish glitter",
                "Snacks" => "ethically sourced swamp chips",
                _ => "involving polite eels"
            };

            Console.WriteLine($"Topic: {topic} -> {tagline}");
        }

        Console.WriteLine("Agenda bubbles delivered.");
    }
}
