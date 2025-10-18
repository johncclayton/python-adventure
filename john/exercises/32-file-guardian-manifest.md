1. **Purpose**
   Serialize and deserialize JSON using `System.Text.Json` for guardian manifests.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | Serialize object | `JsonSerializer.Serialize(data)` | https://learn.microsoft.com/dotnet/standard/serialization/system-text-json-overview |
   | Deserialize | `JsonSerializer.Deserialize<List<Guardian>>(json)` | https://learn.microsoft.com/dotnet/standard/serialization/system-text-json-deserialize |
   | Configure options | `new JsonSerializerOptions { WriteIndented = true }` | https://learn.microsoft.com/dotnet/standard/serialization/system-text-json-configure-options |

3. **Adventure Story / Problem**
   The undersea customs office now requires a JSON manifest of every guardian entering. They also hand back an existing JSON roster that you must parse to confirm arrivals.

   Build a console app that:
   - Defines a `Guardian` class with `Name`, `Role`, and `GlowstickCount`.
   - Reads JSON from input (single line) representing a list of guardians.
   - Deserializes into objects and prints each in human-friendly form.
   - Creates a new manifest including only guardians with `GlowstickCount` > 0 and prints the JSON with indentation.

4. **Example Input/Output**
   Input:
   ```
   [{"Name":"Bard","Role":"Wi-Fi","GlowstickCount":2}]
   ```

   Output:
   ```
   Arrival: Bard - Wi-Fi - Glowsticks 2
   Manifest:
   [
     {
       "Name": "Bard",
       "Role": "Wi-Fi",
       "GlowstickCount": 2
     }
   ]
   ```

5. **Tone Reminder**
   Picture yourself as a cheerful customs officer stamping glowing passports.