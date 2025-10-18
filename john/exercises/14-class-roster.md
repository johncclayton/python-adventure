1. **Purpose**
   Declare a basic class with auto-properties to represent labyrinth companions.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | Auto-property | public string Name { get; set; } | https://learn.microsoft.com/dotnet/csharp/programming-guide/classes-and-structs/properties |
   | Object initialization | 
ew Companion { Name = "Bard" } | https://learn.microsoft.com/dotnet/csharp/programming-guide/classes-and-structs/object-and-collection-initializers |
   | Constructors | public Companion(string name) | https://learn.microsoft.com/dotnet/csharp/programming-guide/classes-and-structs/constructors |

3. **Adventure Story / Problem**
   Debugsworth wants a roster printout before marching into the next biome. Build a Companion class to hold roster details.

   Requirements:
   - Companion has auto-properties: Name, Specialty, and IsOnDuty (ool).
   - Include a constructor taking 
ame and specialty, defaulting IsOnDuty to 	rue.
   - In Main, create two companions and print lines like "Bard - Wi-Fi Hymns - On duty: True".

4. **Example Input/Output**
   Input: *(none)*

   Output:
   `
   Bard - Wi-Fi Hymns - On duty: True
   Barbarian - Mud Negotiations - On duty: True
   `

5. **Tone Reminder**
   Treat the roster like a proud stage announcement—each companion deserves a spotlight.