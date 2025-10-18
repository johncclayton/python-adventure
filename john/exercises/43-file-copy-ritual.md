1. **Purpose** – New concept: write text with a `using` wrapped `StreamWriter`.
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| StreamWriter with using | `using var writer = new StreamWriter(path);` | [StreamWriter with using](https://learn.microsoft.com/dotnet/api/system.io.streamwriter) |

3. **Adventure Story / Problem** – The gratitude goblin only bows when thank-you notes are penned inside a proper `using` ritual. Use a `StreamWriter` inside a `using` declaration to write a thank-you line to a file, then read the file back and print it.

4. **Example Input/Output**

```
Output
Stored thanks: Thanks, labyrinth janitor!
```
