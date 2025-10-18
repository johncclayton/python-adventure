using System;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        await StabilizeAsync("Labyrinth Gate");
        await StabilizeAsync("Undersea Dome");
    }

    private static async Task StabilizeAsync(string room)
    {
        Console.WriteLine($"Stabilizing {room}...");
        await Task.Delay(500);
        Console.WriteLine($"{room} stabilized!");
    }
}
