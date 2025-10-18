using System;

class Program
{
    static void Main()
    {
        var bard = new Companion("Bard", "Wi-Fi Hymns");
        var barbarian = new Companion("Barbarian", "Mud Negotiations");

        Console.WriteLine($"{bard.Name} - {bard.Specialty} - On duty: {bard.IsOnDuty}");
        Console.WriteLine($"{barbarian.Name} - {barbarian.Specialty} - On duty: {barbarian.IsOnDuty}");
    }
}

class Companion
{
    public Companion(string name, string specialty)
    {
        Name = name;
        Specialty = specialty;
        IsOnDuty = true;
    }

    public string Name { get; set; }

    public string Specialty { get; set; }

    public bool IsOnDuty { get; set; }
}
