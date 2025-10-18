1. **Purpose** – New concept: raise and subscribe to events.
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| Events | `bell.Rung += handler;` | [Events](https://learn.microsoft.com/dotnet/csharp/programming-guide/events/) |

3. **Adventure Story / Problem** – The guardian bell only rings when heroes wire up proper event handlers to announce the alarm. Create a class exposing an event. Subscribe with a lambda that prints a message, trigger the event, and ensure the handler fires.

4. **Example Input/Output**

```
Output
Guardian bell: alert the swamp crew!
```
