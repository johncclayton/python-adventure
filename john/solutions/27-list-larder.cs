var supplies = new System.Collections.Generic.List<string> { "hot sauce" };
supplies.Add("extra socks");
supplies.Remove("hot sauce");
foreach (var item in supplies)
{
    Console.WriteLine($"Still packed: {item}");
}
