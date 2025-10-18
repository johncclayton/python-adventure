1. **Purpose**
   Aggregate data with LINQ to tally audience laughter quotas.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | LINQ `.Sum` | `var total = counts.Sum();` | https://learn.microsoft.com/dotnet/api/system.linq.enumerable.sum |
   | LINQ `.GroupBy` | `items.GroupBy(i => i.Room)` | https://learn.microsoft.com/dotnet/api/system.linq.enumerable.groupby |
   | LINQ `.OrderByDescending` | `.OrderByDescending(g => g.Sum(x => x.Count))` | https://learn.microsoft.com/dotnet/api/system.linq.enumerable.orderbydescending |

3. **Adventure Story / Problem**
   The undersea meeting manager demands a report showing total laughs per biome so they can budget jellybean confetti.

   Build a console app that:
   - Creates a list of records `(room, laughs)` describing each set.
   - Groups by room, sums the laughs, orders descending by total.
   - Prints `Room -> total laughs` for each group and a final `Grand total: X`.

4. **Example Input/Output**
   Input: *(none)*

   Output:
   ```
   Labyrinth Arena -> 42 laughs
   Swamp Lounge -> 31 laughs
   Undersea Dome -> 18 laughs
   Grand total: 91
   ```

5. **Tone Reminder**
   Sound like an exuberant statistician tossing confetti charts everywhere.