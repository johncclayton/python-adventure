1. **Purpose**
   Order exception handlers and clean up resources with finally blocks or the using statement.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | Multiple catches | `catch (FormatException) { } catch (Exception) { }` | https://learn.microsoft.com/dotnet/csharp/language-reference/statements/try-catch |
   | using statement | `using var reader = new StringReader(text);` | https://learn.microsoft.com/dotnet/csharp/language-reference/statements/using |
   | finally cleanup | `finally { Console.WriteLine("Done"); }` | https://learn.microsoft.com/dotnet/csharp/language-reference/statements/try-finally |

3. **Adventure Story / Problem**
   Debugsworth tests swamp potions. Some fizz, some explode, all require tidying up the workstation.

   Create a console app that:
   - Reads potion potency (`int`). Potency over 9 should throw an `InvalidOperationException` with message "Potion imploded".
   - Potency below 0 should throw `ArgumentOutOfRangeException`.
   - Catch the specific exceptions to print tailored messages, then catch remaining `Exception` to print a generic warning.
   - Use `finally` to print `Workbench sanitized.` every time.

4. **Example Input/Output**
   Input:
   ```
   12
   ```

   Output:
   ```
   Potion imploded
   Workbench sanitized.
   ```

5. **Tone Reminder**
   Maintain mad-scientist cheer even while cleaning up potion debris.