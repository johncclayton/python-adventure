using System;

class Program
{
    static void Main()
    {
        int torchBrightness = int.Parse(Console.ReadLine() ?? "0");
        int snackSupply = int.Parse(Console.ReadLine() ?? "0");
        int detourMinutes = int.Parse(Console.ReadLine() ?? "0");

        int hazardScore = (detourMinutes * 2) - torchBrightness + snackSupply;
        bool needsBackup = hazardScore >= 10;

        Console.WriteLine($"Hazard score: {hazardScore}");
        Console.WriteLine($"Backup runners requested: {needsBackup}");
    }
}
