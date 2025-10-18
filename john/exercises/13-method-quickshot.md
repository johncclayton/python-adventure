1. **Purpose**
   Craft sleek expression-bodied members for lightweight formatting spells.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | Expression-bodied method | static string Format() => "Result"; | https://learn.microsoft.com/dotnet/csharp/programming-guide/statements-expression-bodied-members |
   | Expression-bodied property | public string Mood => _mood; | https://learn.microsoft.com/dotnet/csharp/programming-guide/statements-expression-bodied-members |
   | String concatenation | $"{a} {b}" | https://learn.microsoft.com/dotnet/csharp/language-reference/tokens/interpolated |

3. **Adventure Story / Problem**
   Debugsworth is late for rehearsal. He needs a ChantFormatter helper with methods short enough to scribble on a napkin mid-run.

   Implement a class in the same file as Program:
   - ChantFormatter with a constructor accepting string performer.
   - A read-only property Performer using an expression body.
   - A method IntroLine(string venue) that returns "{Performer} reporting to {venue}!" via an expression body.
   - Program.Main should instantiate the formatter with a name from input and print the intro line for "Labyrinth Plaza".

4. **Example Input/Output**
   Input:
   `
   Debugsworth
   `

   Output:
   `
   Debugsworth reporting to Labyrinth Plaza!
   `

5. **Tone Reminder**
   Keep it snappy—the hero is literally running down a hallway while reading your code.