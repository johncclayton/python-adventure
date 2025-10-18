1. **Purpose**
   Flex the core arithmetic and comparison operators while calculating maze-wandering risk scores.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | Arithmetic | int total = torches + snacks - detours; | https://learn.microsoft.com/dotnet/csharp/language-reference/operators/arithmetic-operators |
   | Comparison | ool isLate = currentHour >= curfewHour; | https://learn.microsoft.com/dotnet/csharp/language-reference/operators/comparison-operators |
   | Logical operators | if (isLate && !hasPass) | https://learn.microsoft.com/dotnet/csharp/language-reference/operators/boolean-logical-operators |

3. **Adventure Story / Problem**
   The maze toll troll hands Debugsworth a worksheet demanding tonight's hazard index. If the math looks wrong, the gate slams shut until sunrise.

   Build a console app that:
   - Reads three integers from standard input: torch brightness, snack supply, and detour minutes.
   - Computes a hazard score: (detourMinutes * 2) - torchBrightness + snackSupply.
   - Compares the score against the threshold 10. If the score is greater than or equal, set a ool 
eedsBackup to 	rue.
   - Print two lines: one showing the computed score, another announcing whether backup runners are dispatched.

4. **Example Input/Output**
   Input:
   `
   6
   4
   8
   `

   Output:
   `
   Hazard score: 10
   Backup runners requested: True
   `

5. **Tone Reminder**
   Keep the narration urgent yet playful—nobody likes a sulky troll accountant.