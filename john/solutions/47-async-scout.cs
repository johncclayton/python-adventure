await BeaconAsync();

static async Task BeaconAsync()
{
    Console.WriteLine("Preparing ping...");
    await Task.Delay(50);
    Console.WriteLine("Ping sent!");
}
