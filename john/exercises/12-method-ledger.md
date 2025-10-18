1. **Purpose**
   Experiment with ef and out parameters to modify swamp briefing stats in-place.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | ef parameter | static void Boost(ref int torches) | https://learn.microsoft.com/dotnet/csharp/language-reference/keywords/ref |
   | out parameter | static bool TryCalm(string input, out int calmLevel) | https://learn.microsoft.com/dotnet/csharp/language-reference/keywords/out |
   | TryParse pattern | int.TryParse(value, out var result) | https://learn.microsoft.com/dotnet/api/system.int32.tryparse |

3. **Adventure Story / Problem**
   The swamp quartermaster hands Debugsworth a soggy ledger. You must bump the torch count and interpret a mud rating scribble without creating a new ledger copy.

   Build a console app that:
   - Declares an int torches = 3; and a string mudRating from input.
   - Calls BoostTorch(ref torches) to add 2 torches.
   - Calls TryInterpretMud(mudRating, out int level) which returns 	rue if the string parses to an int between 0 and 10.
   - Prints the updated torch count and either Mud level interpreted: X or Mud level unreadable. depending on the method result.

4. **Example Input/Output**
   Input:
   `
   7
   `

   Output:
   `
   Torches ready: 5
   Mud level interpreted: 7
   `

5. **Tone Reminder**
   Think of yourself as the swamp's data wizard—calmly mutating values while cracking a grin.