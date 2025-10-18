1. **Purpose**
   Read text files safely and summarize their contents.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | File read | `var lines = File.ReadAllLines(path);` | https://learn.microsoft.com/dotnet/api/system.io.file.readalllines |
   | Path combine | `Path.Combine(baseDir, "notes.txt")` | https://learn.microsoft.com/dotnet/api/system.io.path.combine |
   | Exception handling | `catch (IOException ex)` | https://learn.microsoft.com/dotnet/standard/io/handling-io-errors |

3. **Adventure Story / Problem**
   Debugsworth discovers a folder of heckler reviews. He needs a tool to read them and count the number of cheers vs jeers.

   Build a console app that:
   - Reads a file path from input.
   - Uses `File.ReadAllLines` inside a `try/catch` to load the file. On failure, print `Reading failed: message`.
   - Counts lines containing `cheer` vs `jeer` (case-insensitive) and prints both totals.

4. **Example Input/Output**
   Input:
   ```
   reviews.txt
   ```

   Output:
   ```
   Cheers spotted: 4
   Jeers spotted: 1
   ```

5. **Tone Reminder**
   Approach it like a curious archivist delighting in audience drama.