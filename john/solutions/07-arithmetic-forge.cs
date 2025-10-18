int collected = 10;
int lost = 2;
int repaired = collected - lost;
int doubled = repaired * 2;
int remainder = doubled % 2;
Console.WriteLine($"Repaired: {repaired}");
Console.WriteLine($"Doubled: {doubled}");
Console.WriteLine($"Split remainder: {remainder}");
