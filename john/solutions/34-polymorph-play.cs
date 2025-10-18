var performers = new System.Collections.Generic.List<IPerformer>
{
    new BardPerformer(),
    new GoblinPerformer()
};

foreach (var performer in performers)
{
    Console.WriteLine($"Performance: {performer.Perform()}");
}

interface IPerformer
{
    string Perform();
}

class BardPerformer : IPerformer
{
    public string Perform() => "Bard strums wifi blues";
}

class GoblinPerformer : IPerformer
{
    public string Perform() => "Goblin beatboxes bug fixes";
}

