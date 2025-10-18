var path = "thanks.txt";
using (var writer = new System.IO.StreamWriter(path))
{
    writer.WriteLine("Thanks, labyrinth janitor!");
}
Console.WriteLine($"Stored thanks: {System.IO.File.ReadAllText(path).Trim()}");
