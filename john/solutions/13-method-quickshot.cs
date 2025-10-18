using System;

class Program
{
    static void Main()
    {
        string performerName = Console.ReadLine() ?? string.Empty;
        var formatter = new ChantFormatter(performerName);

        Console.WriteLine(formatter.IntroLine("Labyrinth Plaza"));
    }
}

class ChantFormatter
{
    private readonly string _performer;

    public ChantFormatter(string performer) => _performer = performer;

    public string Performer => _performer;

    public string IntroLine(string venue) => $"{Performer} reporting to {venue}!";
}
