var cts = new System.Threading.CancellationTokenSource();
var task = ScanAsync(cts.Token);
cts.Cancel();
try
{
    await task;
}
catch (OperationCanceledException)
{
    Console.WriteLine("Scan canceled politely.");
}

static async Task ScanAsync(System.Threading.CancellationToken token)
{
    token.ThrowIfCancellationRequested();
    await Task.Delay(10, token);
    Console.WriteLine("Scan completed.");
}
