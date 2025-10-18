1. **Purpose**
   Declare custom delegates and pass behavior into scheduling helpers.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | Delegate declaration | `public delegate void ChantAction(string target);` | https://learn.microsoft.com/dotnet/csharp/programming-guide/delegates/using-delegates |
   | Passing delegates | `RunChant(chant);` | https://learn.microsoft.com/dotnet/csharp/programming-guide/delegates/passing-delegates-as-arguments |
   | Lambda expressions | `name => Console.WriteLine(name)` | https://learn.microsoft.com/dotnet/csharp/lambda-expressions |

3. **Adventure Story / Problem**
   The rehearsal coordinator wants a scriptable chant scheduler: pass in a behavior, get a dramatic announcement.

   Build:
   - Delegate `public delegate void ChantAction(string target);`
   - Method `ExecuteChant(string guardian, ChantAction action)` that writes `"Summoning guardian"` then invokes `action`.
   - In `Main`, call `ExecuteChant` with a lambda printing `"{guardian} responds with gusto!"` and again with another lambda referencing a local counter.

4. **Example Input/Output**
   Input: *(none)*

   Output:
   ```
   Summoning Bard
   Bard responds with gusto!
   Summoning Barbarian
   Barbarian responds with gusto level 2!
   ```

5. **Tone Reminder**
   Delight in the theatrical flexibility—you're choreographing call-and-response routines.