var convoy = new Caravan("Debugsworth", 2);
Console.WriteLine($"Leader: {convoy.Leader}");
Console.WriteLine($"Wagons: {convoy.Wagons}");

class Caravan
{
    public Caravan(string leader, int wagons)
    {
        Leader = leader;
        Wagons = wagons;
    }

    public string Leader { get; }
    public int Wagons { get; }
}
