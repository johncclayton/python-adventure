1. **Purpose**
   Respond to cancellation tokens during long-running undersea bubble scans.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | Cancellation token | `CancellationTokenSource cts = new();` | https://learn.microsoft.com/dotnet/standard/threading/cancellation-in-managed-threads |
   | Passing token | `await ScanAsync(cts.Token);` | https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken |
   | Observing cancellation | `token.ThrowIfCancellationRequested();` | https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken.throwifcancellationrequested |

3. **Adventure Story / Problem**
   The eel auditors demand a bubble scan but may cancel it if an emergency stand-up meeting appears. Your code must stay polite and responsive.

   Build a console app that:
   - Starts a `CancellationTokenSource` that cancels after 1 second using `CancelAfter`.
   - Runs an async method that loops five times, awaiting `Task.Delay(400)` each iteration and checking `token.ThrowIfCancellationRequested()`.
   - Catch `OperationCanceledException` to print `Scan aborted by eel.`

4. **Example Input/Output**
   Input: *(none)*

   Output:
   ```
   Bubble scan tick 1
   Bubble scan tick 2
   Scan aborted by eel.
   ```

5. **Tone Reminder**
   Keep the reporting courteous—the eel auditors appreciate professionalism even when cancelling you.