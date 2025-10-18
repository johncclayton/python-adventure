using System;

class Program
{
    static void Main()
    {
        var firstPlan = new TravelPlan("Bard");
        var secondPlan = new TravelPlan("Barbarian", "eelback", 21);

        Console.WriteLine(firstPlan.ToSummary());
        Console.WriteLine(secondPlan.ToSummary());
    }
}

class TravelPlan
{
    public TravelPlan(string name)
        : this(name, "echo-wagon", 19)
    {
    }

    public TravelPlan(string name, string mode, int departureHour)
    {
        Name = name;
        Mode = mode;
        DepartureHour = departureHour;
    }

    public string Name { get; }

    public string Mode { get; }

    public int DepartureHour { get; }

    public string ToSummary() => $"{Name} via {Mode} at {DepartureHour:00}:00";
}
