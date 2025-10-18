1. **Purpose** – New concept: filter sequences with LINQ `Where`.
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| LINQ Where | `var calmRooms = rooms.Where(r => r.Contains("Calm"));` | [LINQ Where](https://learn.microsoft.com/dotnet/csharp/programming-guide/concepts/linq/) |

3. **Adventure Story / Problem** – A scoutfish only relays calm meeting rooms if John filters the full reef schedule with fluent LINQ magic. Create an array of room names and use `Where` to keep only those containing the word `Calm`. Iterate the filtered results and print each one.

4. **Example Input/Output**

```
Output
Calm Coral Council
```
