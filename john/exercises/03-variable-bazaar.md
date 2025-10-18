1. **Purpose**
   Practice declaring variables of different primitive types and celebrating them with string interpolation.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | Primitive declaration | int torchCount = 3; | https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/value-types |
   | Type inference with ar | ar swampTemp = 18.5; | https://learn.microsoft.com/dotnet/csharp/fundamentals/types/usage-of-the-var-keyword |
   | String interpolation | $"Torches: {torchCount}" | https://learn.microsoft.com/dotnet/csharp/language-reference/tokens/interpolated |

3. **Adventure Story / Problem**
   Debugsworth pauses at a crossroad kiosk run by sarcastic vines. They will only hand over the next maze map if you deliver a status board summarizing tonight's expedition supplies.

   Build a console app that:
   - Declares an int for torch count, a double for swamp temperature, and a ool flag indicating if the frog choir is booked.
   - Uses ar to hold a string describing the current biome name.
   - Prints a single interpolated sentence like "Labyrinth Hub: 5 torches, swamp temp 18.5°C, frog choir booked: True."
   - Ends with a reassuring Console.WriteLine("All supplies logged.");

4. **Example Input/Output**
   Input: *(none)*

   Output:
   `
   Labyrinth Hub: 5 torches, swamp temp 18.5°C, frog choir booked: True.
   All supplies logged.
   `

5. **Tone Reminder**
   Make the status readout feel like a confident field briefing—those vines love professionalism.