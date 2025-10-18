int currentSpeed = 12;
string strategy = currentSpeed switch
{
    int level when level > 10 => "Strategy: anchor the chairs.",
    int level when level > 5 => "Strategy: hand out snorkels.",
    _ => "Strategy: serve tea slowly."
};
Console.WriteLine(strategy);
