1. **Purpose**
   Map keys to values with a dictionary to assign guardians to rooms.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | Dictionary setup | ar map = new Dictionary<string, string>(); | https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2 |
   | Add entries | map["Labyrinth"] = "Bard"; | https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2.item |
   | Lookup with TryGetValue | map.TryGetValue(room, out var guardian) | https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2.trygetvalue |

3. **Adventure Story / Problem**
   The comedy show producer needs a quick lookup to see which guardian is stationed at each venue room.

   Build a console app that:
   - Seeds a dictionary with three room-to-guardian assignments.
   - Reads a room name from input and prints the guardian if found.
   - If missing, print No guardian scheduled. Summon the intern.
   - After answering the query, print every assignment sorted alphabetically by room.

4. **Example Input/Output**
   Input:
   `
   Swamp Lounge
   `

   Output:
   `
   Guardian on duty: Barbarian
   Undersea Dome -> Mimic Chest
   Labyrinth Hub -> Bard
   Swamp Lounge -> Barbarian
   `

5. **Tone Reminder**
   Imagine you're the show's stage manager—efficient, cheerful, and ready with backups.