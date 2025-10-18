1. **Purpose**
   Raise and subscribe to events so the guardians can react to alert bells.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | Event declaration | `public event EventHandler BellRang;` | https://learn.microsoft.com/dotnet/csharp/programming-guide/events/ |
   | Raising events | `BellRang?.Invoke(this, EventArgs.Empty);` | https://learn.microsoft.com/dotnet/csharp/programming-guide/events/how-to-raise-and-consume-events |
   | Event subscription | `bell.BellRang += OnBellRang;` | https://learn.microsoft.com/dotnet/csharp/programming-guide/events/how-to-subscribe-to-and-unsubscribe-from-events |

3. **Adventure Story / Problem**
   The labyrinth installs a magical bell. When it rings, on-duty guardians should perform their rehearsed responses.

   Build:
   - Class `AlertBell` with event `EventHandler<string>` named `BellRang` that passes the bell location.
   - Method `Ring(string location)` that prints `"Bell ringing at location"` then raises the event.
   - In `Main`, subscribe two handlers that print unique reactions and trigger at least twice.

4. **Example Input/Output**
   Input: *(none)*

   Output:
   ```
   Bell ringing at Labyrinth Gate
   Bard tunes the network lute for Labyrinth Gate
   Barbarian readies mud shields for Labyrinth Gate
   Bell ringing at Undersea Dome
   Bard tunes the network lute for Undersea Dome
   Barbarian readies mud shields for Undersea Dome
   ```

5. **Tone Reminder**
   Sound like an emergency drill instructor who still knows how to hype a crowd.