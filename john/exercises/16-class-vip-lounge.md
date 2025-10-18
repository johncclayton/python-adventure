1. **Purpose**
   Practice access modifiers by guarding the labyrinth's VIP lounge checklist.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | private field | private int secret; | https://learn.microsoft.com/dotnet/csharp/language-reference/keywords/private |
   | internal class | internal class LoungeChecklist | https://learn.microsoft.com/dotnet/csharp/language-reference/keywords/internal |
   | Encapsulated method | public bool CanEnter(string name) | https://learn.microsoft.com/dotnet/csharp/programming-guide/classes-and-structs/access-modifiers |

3. **Adventure Story / Problem**
   Debugsworth must manage a hush-hush lounge where only VIPs may sip sparkling swamp tea. The bouncer demands software with proper doors and locks.

   Build an internal class LoungeChecklist:
   - Store a private readonly HashSet<string> of allowed names (seed in constructor).
   - Expose a public bool CanEnter(string name) that checks membership case-insensitively.
   - Provide a public string Describe() returning "VIPs: name1, name2".
   - Main should instantiate the checklist, read a name from input, print the description, then print either Welcome name! or Sorry name. depending on CanEnter.

4. **Example Input/Output**
   Input:
   `
   Mimic Chest
   `

   Output:
   `
   VIPs: Bard, Mimic Chest
   Welcome Mimic Chest!
   `

5. **Tone Reminder**
   Think secretive yet kind—like a bouncer who moonlights as an etiquette coach.