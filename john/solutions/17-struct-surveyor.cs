using System;

class Program
{
    static void Main()
    {
        var origin = new MazePoint(2, 5);
        var offset = origin.WithOffset(3, 4);

        Console.WriteLine($"Original: ({origin.X}, {origin.Y})");
        Console.WriteLine($"Offset: ({offset.X}, {offset.Y})");
    }
}

public readonly struct MazePoint
{
    public MazePoint(int x, int y)
    {
        X = x;
        Y = y;
    }

    public int X { get; }

    public int Y { get; }

    public MazePoint WithOffset(int dx, int dy) => new MazePoint(X + dx, Y + dy);
}
