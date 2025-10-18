1. **Purpose**
   Combine comparisons with logical operators to make confident go/no-go decisions.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | &&, ||, ! | if (torches >= 3 && !mudAlert) | https://learn.microsoft.com/dotnet/csharp/language-reference/operators/boolean-logical-operators |
   | Nested conditions | if (...) { ... } else if (...) | https://learn.microsoft.com/dotnet/csharp/language-reference/statements/selection-statements |
   | Parsing numbers | int.Parse(Console.ReadLine()!) | https://learn.microsoft.com/dotnet/csharp/how-to/parse-strings |

3. **Adventure Story / Problem**
   The Sarcastic Swamp's concierge frog only opens the gate for parties that meet a strict checklist. Tilt one lever wrong and you'll get roasted by amphibian sarcasm.

   Create a console app that:
   - Reads three lines: torch count (int), boots are waterproof (	rue/alse), and mud forecast level (int).
   - Approves entry if torch count is at least 2 **and** boots are waterproof **and** mud forecast is below 7.
   - If entry is denied but mud forecast is under 4, print a consolation line inviting them to "grab extra towels".
   - Always print Entry granted! or Entry denied! as the first output line and append any consolation line second.

4. **Example Input/Output**
   Input:
   `
   2
   true
   5
   `

   Output:
   `
   Entry denied!
   Grab extra towels before reapplying.
   `

5. **Tone Reminder**
   Channel your inner concierge: brisk, witty, and unflappable in the face of mud forecasts.