1. **Purpose**
   Exercise multiple interface implementations and runtime dispatch for the guardian logistics team.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | Multiple interfaces | class Bard : IPerformer, ILogistics | https://learn.microsoft.com/dotnet/csharp/fundamentals/object-oriented/interfaces#implementing-multiple-interfaces |
   | Casting to interface | if (actor is ILogistics mover) | https://learn.microsoft.com/dotnet/csharp/fundamentals/types/is |
   | Virtual method override | public override string Describe() | https://learn.microsoft.com/dotnet/csharp/language-reference/keywords/virtual |

3. **Adventure Story / Problem**
   For the grand finale, Debugsworth needs both a stage act and a logistics briefing from the same lineup. Some guardians multitask, others do not.

   Build:
   - Base class Guardian with virtual DescribeDuty().
   - Interface ILogistics with string PlanRoute().
   - Subclasses BardGuardian, BarbarianGuardian, and MimicChestGuardian. Only some implement ILogistics.
   - In Main, loop through guardians printing DescribeDuty(). When a guardian implements ILogistics, also print their PlanRoute() result.

4. **Example Input/Output**
   Input: *(none)*

   Output:
   `
   Bard duty: Calm the Wi-Fi spirits.
   Bard logistics: Route cables through cheering crowd.
   Barbarian duty: Keep mud morale high.
   Mimic Chest duty: Manage surprise agenda crates.
   Mimic Chest logistics: Sneak routes via air ducts.
   `

5. **Tone Reminder**
   Narrate like a head of operations who still appreciates theatrical flair.