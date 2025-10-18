1. **Purpose**
   Practice chaining if/else branches to route Debugsworth through the right biome gateway.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | if/else if/else | if (choice == "maze") ... else if ... | https://learn.microsoft.com/dotnet/csharp/language-reference/statements/selection-statements |
   | Trimming strings | ar path = input.Trim(); | https://learn.microsoft.com/dotnet/api/system.string.trim |
   | Case-insensitive compare | Equals(value, StringComparison.OrdinalIgnoreCase) | https://learn.microsoft.com/dotnet/api/system.string.equals |

3. **Adventure Story / Problem**
   The Labyrinth Transit Authority offers three portals, but only one leads to tonight's scheduled comedy roast. Debugsworth needs your routing brain to avoid the eel-led budget meeting.

   Build a console app that:
   - Reads a single line describing the traveler mood ("brave", "tired", or "curious").
   - Uses an if/else if/else chain to determine the destination:
     - brave -> "Labyrinth Arena"
     - tired -> "Swamp Sauna"
     - curious -> "Undersea Archives"
     - anything else -> "Lobby of Lost Socks"
   - Print Escorting to: DESTINATION
   - For unknown moods, also print Recommendation: fill out the vibe questionnaire.

4. **Example Input/Output**
   Input:
   `
   curious
   `

   Output:
   `
   Escorting to: Undersea Archives
   `

5. **Tone Reminder**
   Keep your escort voice confident—the maze riders need to believe you know every corridor.