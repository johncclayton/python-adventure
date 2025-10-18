LabGear pack = LabGear.Lantern | LabGear.Boots;
Console.WriteLine($"Pack includes: {pack}");

[Flags]
enum LabGear
{
    None = 0,
    Lantern = 1,
    Map = 2,
    Boots = 4
}
