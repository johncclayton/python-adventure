using System;
using System.Threading;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        using var cts = new CancellationTokenSource();
        cts.CancelAfter(TimeSpan.FromSeconds(1));

        try
        {
            await BubbleScanAsync(cts.Token);
            Console.WriteLine("Bubble scan completed.");
        }
        catch (OperationCanceledException)
        {
            Console.WriteLine("Scan aborted by eel.");
        }
    }

    private static async Task BubbleScanAsync(CancellationToken token)
    {
        for (int i = 0; i < 5; i++)
        {
            token.ThrowIfCancellationRequested();
            Console.WriteLine($"Bubble scan tick {i + 1}");
            await Task.Delay(400, token);
        }
    }
}
