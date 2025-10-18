var vector = new RuneVector(1, -1);
Console.WriteLine($"Vector row: {vector.Row}");
Console.WriteLine($"Vector column: {vector.Column}");

readonly struct RuneVector
{
    public RuneVector(int row, int column)
    {
        Row = row;
        Column = column;
    }

    public int Row { get; }
    public int Column { get; }
}
