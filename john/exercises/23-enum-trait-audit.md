1. **Purpose**
   Combine bit flags to describe multi-trait guardians without losing nuance.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | [Flags] enum | [Flags] enum Traits { ... } | https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/enum#flags-enums |
   | Bitwise OR | Traits.Musical | Traits.MoistureProof | https://learn.microsoft.com/dotnet/csharp/language-reference/operators/bitwise-and-shift-operators |
   | Checking flags | 	raits.HasFlag(Traits.Musical) | https://learn.microsoft.com/dotnet/api/system.enum.hasflag |

3. **Adventure Story / Problem**
   The stage safety inspector tracks guardian traits (musical, waterproof, glow-in-the-dark). Generate a flag report to appease them.

   Build a console app that:
   - Declares [Flags] enum GuardianTraits { None = 0, Musical = 1, Waterproof = 2, Glow = 4 }.
   - Creates a dictionary mapping guardian names to their trait combos.
   - Reads a guardian name, prints the combined traits, and states whether they are waterproof.

4. **Example Input/Output**
   Input:
   `
   Bard
   `

   Output:
   `
   Traits: Musical, Glow
   Waterproof? No
   `

5. **Tone Reminder**
   Adopt the voice of a clipboard-wielding inspector who still enjoys a good pun.