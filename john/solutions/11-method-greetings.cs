using System;

class Program
{
    static void Main()
    {
        string name = Console.ReadLine() ?? string.Empty;

        Console.WriteLine(BuildSalute(name));
        Console.WriteLine(BuildEncore(name));
    }

    private static string BuildSalute(string name) => $"Saluting mighty {name}!";

    private static string BuildEncore(string name) => $"Encore requested by {name}.";
}
