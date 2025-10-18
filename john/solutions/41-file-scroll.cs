var path = "scroll.txt";
System.IO.File.WriteAllText(path, "Labyrinth memo\nSwamp memo");
string[] lines = System.IO.File.ReadAllLines(path);
Console.WriteLine($"Line 1: {lines[0]}");
Console.WriteLine($"Line 2: {lines[1]}");
