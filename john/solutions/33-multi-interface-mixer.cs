IMoodReporter reporter = new MimicChest();
IAlarmRaiser alarm = new MimicChest();
Console.WriteLine($"Report: {reporter.Describe()}");
Console.WriteLine($"Alarm: {alarm.Trigger()}");

interface IMoodReporter
{
    string Describe();
}

interface IAlarmRaiser
{
    string Trigger();
}

class MimicChest : IMoodReporter, IAlarmRaiser
{
    public string Describe() => "Mood stable";
    public string Trigger() => "Confetti deployed";
}
