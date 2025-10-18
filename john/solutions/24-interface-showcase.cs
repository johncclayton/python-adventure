using System;
using System.Collections.Generic;

interface IPerformer
{
    string Name { get; }
    string Perform();
}

class BardPerformer : IPerformer
{
    public string Name => "Bard";

    public string Perform() => "Router ballad with improvised packets";
}

class BarbarianPerformer : IPerformer
{
    public string Name => "Barbarian";

    public string Perform() => "Motivational axe choreography";
}

class MimicChestPerformer : IPerformer
{
    public string Name => "Mimic Chest";

    public string Perform() => "Surprise status update chorus";
}

class Program
{
    static void Main()
    {
        var lineup = new List<IPerformer>
        {
            new BardPerformer(),
            new BarbarianPerformer(),
            new MimicChestPerformer()
        };

        foreach (var performer in lineup)
        {
            Console.WriteLine($"Next up: {performer.Name} -> {performer.Perform()}");
        }
    }
}
