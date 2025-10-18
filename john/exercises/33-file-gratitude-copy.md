1. **Purpose**
   Manage file streams with the `using` statement to guarantee cleanup.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | `using` declaration | `using var stream = File.OpenRead(path);` | https://learn.microsoft.com/dotnet/csharp/language-reference/statements/using |
   | StreamReader usage | `using var reader = new StreamReader(stream);` | https://learn.microsoft.com/dotnet/api/system.io.streamreader |
   | Writing files | `await File.WriteAllTextAsync(path, text);` | https://learn.microsoft.com/dotnet/api/system.io.file.writealltextasync |

3. **Adventure Story / Problem**
   Debugsworth wants to copy the nightly heckler log into a calmer "gratitude" file, but the swamp union insists on zero dangling streams.

   Build a console app that:
   - Reads two paths: source and destination.
   - Uses `using` declarations with `StreamReader` and `StreamWriter` to copy the lines, prefixing each with `"Grateful note: "`.
   - Prints `Copy complete.` when done.

4. **Example Input/Output**
   Input:
   ```
   jeers.txt
   gratitude.txt
   ```

   Output:
   ```
   Copy complete.
   ```

5. **Tone Reminder**
   Treat the operation like a mindfulness exercise—calming snark into gratitude.