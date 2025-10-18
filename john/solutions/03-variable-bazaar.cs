using System;

class Program
{
    static void Main()
    {
        int torchCount = 5;
        double swampTemperature = 18.5;
        bool frogChoirBooked = true;
        var biomeName = "Labyrinth Hub";

        Console.WriteLine($"{biomeName}: {torchCount} torches, swamp temp {swampTemperature}C, frog choir booked: {frogChoirBooked}.");
        Console.WriteLine("All supplies logged.");
    }
}
