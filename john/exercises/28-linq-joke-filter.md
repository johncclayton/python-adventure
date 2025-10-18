1. **Purpose**
   Filter collections with LINQ to pick tonight's labyrinth jokes.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | LINQ `.Where` | `var filtered = jokes.Where(j => j.Contains("maze"));` | https://learn.microsoft.com/dotnet/csharp/programming-guide/concepts/linq/overview-of-linq |
   | LINQ `.Select` | `var titles = shows.Select(s => s.Title);` | https://learn.microsoft.com/dotnet/csharp/programming-guide/concepts/linq/basic-linq-query-operations |
   | Enumerable materialization | `filtered.ToList()` | https://learn.microsoft.com/dotnet/api/system.linq.enumerable.tolist |

3. **Adventure Story / Problem**
   Debugsworth only wants jokes that mention the maze and are under 40 characters so the Minotaur doesn't lose Wi-Fi.

   Build a console app that:
   - Seeds an array of joke strings.
   - Uses LINQ to select jokes containing "maze" (case-insensitive) and with length < 40, projecting them into `"Approved: {joke}"`.
   - Prints each approved joke, then prints `Total approved: X`.

4. **Example Input/Output**
   Input: *(none)*

   Output:
   ```
   Approved: The maze has better signals than my phone.
   Approved: Maze maintenance is just wall hugging.
   Total approved: 2
   ```

5. **Tone Reminder**
   Imagine you're programming a wise-cracking jukebox—efficient, selective, and amused.