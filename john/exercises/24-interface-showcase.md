1. **Purpose**
   Design interfaces describing performance routines and implement them with quirky guardians.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | Interface declaration | interface IPerformer { void Perform(); } | https://learn.microsoft.com/dotnet/csharp/language-reference/keywords/interface |
   | Implement interface | class Bard : IPerformer | https://learn.microsoft.com/dotnet/csharp/programming-guide/interfaces/ |
   | Polymorphic calls | List<IPerformer> | https://learn.microsoft.com/dotnet/csharp/fundamentals/object-oriented/polymorphism |

3. **Adventure Story / Problem**
   The comedy showcase needs a lineup generator that treats all acts through a shared interface so the emcee can introduce them blindly.

   Build:
   - IPerformer with string Name { get; } and string Perform().
   - Implementations BardPerformer, BarbarianPerformer, MimicChestPerformer each returning a unique routine description.
   - In Main, create a List<IPerformer> and loop to print Next up: Name -> Routine.

4. **Example Input/Output**
   Input: *(none)*

   Output:
   `
   Next up: Bard -> Router ballad with improvised packets
   Next up: Barbarian -> Motivational axe choreography
   Next up: Mimic Chest -> Surprise status update chorus
   `

5. **Tone Reminder**
   Channel an enthusiastic showrunner introducing crowd favorites one after another.