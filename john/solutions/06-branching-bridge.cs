using System;

class Program
{
    static void Main()
    {
        string moodInput = Console.ReadLine() ?? string.Empty;
        string mood = moodInput.Trim();

        string destination;
        if (string.Equals(mood, "brave", StringComparison.OrdinalIgnoreCase))
        {
            destination = "Labyrinth Arena";
        }
        else if (string.Equals(mood, "tired", StringComparison.OrdinalIgnoreCase))
        {
            destination = "Swamp Sauna";
        }
        else if (string.Equals(mood, "curious", StringComparison.OrdinalIgnoreCase))
        {
            destination = "Undersea Archives";
        }
        else
        {
            destination = "Lobby of Lost Socks";
            Console.WriteLine($"Escorting to: {destination}");
            Console.WriteLine("Recommendation: fill out the vibe questionnaire.");
            return;
        }

        Console.WriteLine($"Escorting to: {destination}");
    }
}
