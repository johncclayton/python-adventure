1. **Purpose**
   Write and await asynchronous methods to simulate magical Wi-Fi stabilization.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | Async method | `static async Task CalmAsync()` | https://learn.microsoft.com/dotnet/csharp/programming-guide/concepts/async/ |
   | Awaiting | `await CalmAsync();` | https://learn.microsoft.com/dotnet/csharp/programming-guide/concepts/async/async-and-await |
   | Task delay | `await Task.Delay(500);` | https://learn.microsoft.com/dotnet/api/system.threading.tasks.task.delay |

3. **Adventure Story / Problem**
   Before each show, Debugsworth runs a stabilizer spell that pulses the Wi-Fi crystals. It takes time, so the console app should await it instead of freezing the UI (aka the hero's monologue).

   Build a console app that:
   - Defines `static async Task StabilizeAsync(string room)` that prints start/end messages with a short `Task.Delay` in between.
   - In `Main`, await two stabilization calls sequentially.
   - Ensure `Main` is `static async Task` and invoked with `await StabilizeAsync(...)`.

4. **Example Input/Output**
   Input: *(none)*

   Output:
   ```
   Stabilizing Labyrinth Gate...
   Labyrinth Gate stabilized!
   Stabilizing Undersea Dome...
   Undersea Dome stabilized!
   ```

5. **Tone Reminder**
   Deliver the log lines like a patient wizard monitoring crystal progress bars.