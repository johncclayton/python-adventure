var room = new HeroQuarters { Name = "Labyrinth Loft", CourageScore = 9 };
Console.WriteLine($"Room: {room.Name}");
Console.WriteLine($"Courage: {room.CourageScore}");

class HeroQuarters
{
    public string Name { get; set; } = string.Empty;
    public int CourageScore { get; set; }
}
