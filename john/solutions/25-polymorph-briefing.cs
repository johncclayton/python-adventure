using System;
using System.Collections.Generic;

interface ILogistics
{
    string PlanRoute();
}

abstract class Guardian
{
    protected Guardian(string name)
    {
        Name = name;
    }

    public string Name { get; }

    public virtual string DescribeDuty() => $"{Name} duty: Maintain readiness.";
}

class BardGuardian : Guardian, ILogistics
{
    public BardGuardian() : base("Bard")
    {
    }

    public override string DescribeDuty() => "Bard duty: Calm the Wi-Fi spirits.";

    public string PlanRoute() => "Route cables through cheering crowd.";
}

class BarbarianGuardian : Guardian
{
    public BarbarianGuardian() : base("Barbarian")
    {
    }

    public override string DescribeDuty() => "Barbarian duty: Keep mud morale high.";
}

class MimicChestGuardian : Guardian, ILogistics
{
    public MimicChestGuardian() : base("Mimic Chest")
    {
    }

    public override string DescribeDuty() => "Mimic Chest duty: Manage surprise agenda crates.";

    public string PlanRoute() => "Sneak routes via air ducts.";
}

class Program
{
    static void Main()
    {
        var guardians = new List<Guardian>
        {
            new BardGuardian(),
            new BarbarianGuardian(),
            new MimicChestGuardian()
        };

        foreach (var guardian in guardians)
        {
            Console.WriteLine(guardian.DescribeDuty());
            if (guardian is ILogistics logistics)
            {
                Console.WriteLine($"{guardian.Name} logistics: {logistics.PlanRoute()}");
            }
        }
    }
}
