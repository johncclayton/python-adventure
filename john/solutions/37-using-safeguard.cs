using var reader = new System.IO.StringReader("Labyrinth logs\nSwamp minutes");
Console.WriteLine($"First line: {reader.ReadLine()}");
Console.WriteLine($"Second line: {reader.ReadLine()}");
