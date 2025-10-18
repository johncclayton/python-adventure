BiomeMood mood = BiomeMood.Curious;
int numeric = (int)mood;
BiomeMood parsed = Enum.Parse<BiomeMood>("Snarky");
Console.WriteLine($"Numeric mood: {numeric}");
Console.WriteLine($"Parsed mood: {parsed}");

enum BiomeMood
{
    Calm = 0,
    Curious = 1,
    Snarky = 2
}
