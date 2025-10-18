using System;

delegate void ChantAction(string guardian);

class Program
{
    static void Main()
    {
        ExecuteChant("Bard", name => Console.WriteLine($"{name} responds with gusto!"));

        int callCount = 0;
        ExecuteChant("Barbarian", name =>
        {
            callCount++;
            Console.WriteLine($"{name} responds with gusto level {callCount}!");
        });
    }

    private static void ExecuteChant(string guardian, ChantAction action)
    {
        Console.WriteLine($"Summoning {guardian}");
        action(guardian);
    }
}
