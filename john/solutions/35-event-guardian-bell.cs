using System;

delegate void LocationEventHandler(object? sender, string location);

class AlertBell
{
    public event LocationEventHandler? BellRang;

    public void Ring(string location)
    {
        Console.WriteLine($"Bell ringing at {location}");
        BellRang?.Invoke(this, location);
    }
}

class Program
{
    static void Main()
    {
        var bell = new AlertBell();

        bell.BellRang += (_, location) => Console.WriteLine($"Bard tunes the network lute for {location}");
        bell.BellRang += (_, location) => Console.WriteLine($"Barbarian readies mud shields for {location}");

        bell.Ring("Labyrinth Gate");
        bell.Ring("Undersea Dome");
    }
}
