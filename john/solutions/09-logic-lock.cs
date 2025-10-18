bool hasMap = true;
bool wearingBoots = false;
bool readyToCross = hasMap && !wearingBoots || wearingBoots;
Console.WriteLine($"Crossing ready? {readyToCross}");
