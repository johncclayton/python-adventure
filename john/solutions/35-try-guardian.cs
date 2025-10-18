try
{
    int id = int.Parse("not-a-number");
    Console.WriteLine($"Parsed rune: {id}");
}
catch (FormatException)
{
    Console.WriteLine("Parse failed: invalid rune number.");
}
