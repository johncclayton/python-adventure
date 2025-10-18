var point = new RunePoint(2, 5);
Console.WriteLine($"Rune row: {point.Row}");
Console.WriteLine($"Rune column: {point.Column}");

struct RunePoint
{
    public RunePoint(int row, int column)
    {
        Row = row;
        Column = column;
    }

    public int Row;
    public int Column;
}
