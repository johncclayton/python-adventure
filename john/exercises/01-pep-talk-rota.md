Title: Pep Talk Rota Generator

Briefing:
Sir Johnathan Debugsworth needs a C# console app that assigns the perfect hype-person to each biome on his itinerary. The companions:
- Bard: excels at labyrinth Wi-Fi woes.
- Barbarian: handles snarky swamps by threatening to color-code their mud.
- Mimic Chest: thrives in undersea status meetings and any surprise mud commentary.

Requirements:
1. Read biome names from standard input, one per line. Stop when you hit an empty line.
2. For each biome, choose the companion:
   - Contains "Labyrinth" -> Bard.
   - Contains "Swamp" -> Barbarian.
   - Contains "Undersea" or "Sea" -> Mimic Chest.
   - Default -> Bard (he insists on the spotlight).
3. If the biome text includes "mud" (any casing), schedule an extra Mimic Chest pep talk immediately after the original assignment.
4. Build output lines formatted as `UPPERCASE_BIOME -> Companion (reason)`.
   - Craft a flavorful reason that mentions the matching logic (e.g. "router-stabilizing ballad").
5. Print each line with `Console.WriteLine`.

Hints:
- Use `string.Contains(..., StringComparison.OrdinalIgnoreCase)` for flexible matching.
- Reuse a helper method `GetAssignment(string biome)` that returns multiple lines when the swamp meddles.
- Store outputs in a `List<string>` before writing, so you can append the bonus line easily.

Stretch Goal:
Track how many pep talks each companion gives, and print a final scoreboard line like `Total: Bard 2, Barbarian 1, Mimic Chest 2`.

Deliverable:
Place your program in a new file named `PepTalkRota.cs` and include the `Main` entry point. A reference implementation lives at `john/solutions/01-pep-talk-rota`.
