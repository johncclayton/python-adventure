1. **Purpose**
   Turn a switch expression into a witty biome concierge that maps artifacts to handlers.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | Switch expression | ar result = keyword switch { ... }; | https://learn.microsoft.com/dotnet/csharp/language-reference/operators/switch-expression |
   | Pattern guards | ar => when condition | https://learn.microsoft.com/dotnet/csharp/language-reference/operators/switch-expression#guards |
   | Tuple patterns | (_, var mood) | https://learn.microsoft.com/dotnet/csharp/language-reference/operators/patterns#tuple-pattern |

3. **Adventure Story / Problem**
   As Debugsworth unpacks relics for the night's show-and-tell, the Mimic Chest union insists each item be handed to the correct specialist. You must code the assignment ledger.

   Write a console app that:
   - Reads artifact name and risk level separated by a comma on one line (e.g. "Lantern,3").
   - Uses a switch expression on a tuple (artifactName, riskLevel) to select a handler string:
     - Contains "Lantern" and risk < 5 -> "Router Bard"
     - Contains "Mud" -> "Barbarian Curator"
     - Contains "Scroll" -> "Archivist Eel"
     - Default -> "Intern Gargoyle"
   - Output Handler assigned: HANDLER

4. **Example Input/Output**
   Input:
   `
   Lantern,3
   `

   Output:
   `
   Handler assigned: Router Bard
   `

5. **Tone Reminder**
   Switch expressions should feel like elegant stage directions—snappy and precise.