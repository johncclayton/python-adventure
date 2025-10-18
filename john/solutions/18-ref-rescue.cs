int torches = 3;
Refill(ref torches);
Console.WriteLine($"Torches after refill: {torches}");

static void Refill(ref int torchCount)
{
    torchCount += 2;
}
