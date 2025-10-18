1. **Purpose**
   Define and call static helper methods to keep your console app tidy.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | Static method | static string Summon(int level) { ... } | https://learn.microsoft.com/dotnet/csharp/programming-guide/classes-and-structs/static-classes-and-static-class-members |
   | Method call | ar chant = BuildChant(name); | https://learn.microsoft.com/dotnet/csharp/programming-guide/classes-and-structs/methods |
   | Returning strings | eturn $"Summoning {name}"; | https://learn.microsoft.com/dotnet/csharp/programming-guide/classes-and-structs/methods#return-values |

3. **Adventure Story / Problem**
   Debugsworth wants a ritual script generator that greets specific guardians. Splitting logic into methods will impress the Minotaur stage manager.

   Build a console app that:
   - Reads a single guardian name from input.
   - Calls a static method BuildSalute(string name) that returns a string like "Saluting mighty {name}!".
   - Calls another static method BuildEncore(string name) returning "Encore requested by {name}."
   - Prints both lines from Main.

4. **Example Input/Output**
   Input:
   `
   Minotaur
   `

   Output:
   `
   Saluting mighty Minotaur!
   Encore requested by Minotaur.
   `

5. **Tone Reminder**
   Treat methods like backstage crew—short, capable, and ready on cue.