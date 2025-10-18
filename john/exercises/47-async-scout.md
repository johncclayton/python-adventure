1. **Purpose** – New concept: craft an `async` method that returns `Task` and awaits work.
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| async Task method | `async Task PingAsync() { await Task.Delay(100); }` | [async Task method](https://learn.microsoft.com/dotnet/csharp/programming-guide/concepts/async/) |

3. **Adventure Story / Problem** – A sonar dolphin insists on asynchronous pings so the undersea council is never double-booked. Write an `async` method that awaits `Task.Delay` then prints a confirmation. From top level, await the method so the ping finishes before exiting.

4. **Example Input/Output**

```
Output
Preparing ping...
Ping sent!
```
