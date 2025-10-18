var report = new MeetingReport { Hero = "John", Status = "Prepared" };
string json = System.Text.Json.JsonSerializer.Serialize(report);
Console.WriteLine(json);

class MeetingReport
{
    public string Hero { get; set; } = string.Empty;
    public string Status { get; set; } = string.Empty;
}
