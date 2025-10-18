1. **Purpose** – New concept: read all lines from a text file with `File.ReadAllLines`.
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| File.ReadAllLines | `var lines = File.ReadAllLines(path);` | [File.ReadAllLines](https://learn.microsoft.com/dotnet/api/system.io.file.readalllines) |

3. **Adventure Story / Problem** – The archive turtle only hands over the next clue if John proves he can read a scroll file end-to-end. Write two lines of text to a file, then use `File.ReadAllLines` to load them and print each line with context.

4. **Example Input/Output**

```
Output
Line 1: Labyrinth memo
Line 2: Swamp memo
```
