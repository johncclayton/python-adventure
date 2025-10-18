1. **Purpose**
   Represent discrete mood states using enums for quick swamp diagnostics.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | Enum declaration | num SwampMood { Chill, Snarky } | https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/enum |
   | Parse from string | Enum.TryParse("Chill", out SwampMood mood) | https://learn.microsoft.com/dotnet/api/system.enum.tryparse |
   | Enum to int | (int)SwampMood.Snarky | https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/enum#enum-conversions |

3. **Adventure Story / Problem**
   The mud therapist wants to log swamp moods as tidy enum values, not messy strings.

   Create a console app that:
   - Declares num SwampMood { Chill = 1, Snarky = 2, Chaotic = 3 }.
   - Reads a mood string and parses it; on success, print Mood logged: {mood} ({(int)mood}).
   - On failure, default to Chaotic and print Mood unreadable, defaulting to Chaotic (3).

4. **Example Input/Output**
   Input:
   `
   Snarky
   `

   Output:
   `
   Mood logged: Snarky (2)
   `

5. **Tone Reminder**
   Be the swamp's data whisperer—precise labels, delivered with empathetic charm.