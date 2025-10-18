var bell = new GuardianBell();
bell.Rung += message => Console.WriteLine($"Guardian bell: {message}");
bell.Ring();

class GuardianBell
{
    public event Action<string>? Rung;

    public void Ring()
    {
        Rung?.Invoke("alert the swamp crew!");
    }
}
