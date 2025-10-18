1. **Purpose**
   Manipulate fixed-size arrays to schedule torch relays.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | Array declaration | int[] relay = new int[3]; | https://learn.microsoft.com/dotnet/csharp/programming-guide/arrays/single-dimensional-arrays |
   | Index assignment | elay[0] = 5; | https://learn.microsoft.com/dotnet/csharp/programming-guide/arrays/using-for-each |
   | Array length | elay.Length | https://learn.microsoft.com/dotnet/api/system.array.length |

3. **Adventure Story / Problem**
   Labyrinth fire wardens require a torch handoff schedule showing minutes each runner holds the flame.

   Build a console app that:
   - Creates an int[] of length 3.
   - Reads three integers and stores them in the array.
   - Prints each slot as Runner {index + 1}: {minutes} minutes.
   - Calculates the total and prints Total torch time: X.

4. **Example Input/Output**
   Input:
   `
   5
   7
   4
   `

   Output:
   `
   Runner 1: 5 minutes
   Runner 2: 7 minutes
   Runner 3: 4 minutes
   Total torch time: 16
   `

5. **Tone Reminder**
   Narrate like a proud relay coach with a flair for dramatic pauses.