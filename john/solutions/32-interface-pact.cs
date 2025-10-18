IChant bard = new Bard();
Console.WriteLine($"Chant: {bard.Sing()}");

interface IChant
{
    string Sing();
}

class Bard : IChant
{
    public string Sing() => "Echoing wifi lullaby";
}
