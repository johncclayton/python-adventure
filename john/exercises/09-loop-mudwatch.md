1. **Purpose**
   Use a while loop to tame the swamp's sarcastic mud sensor readings.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | while loop | while (!queue.IsEmpty) | https://learn.microsoft.com/dotnet/csharp/language-reference/statements/iteration-statements#the-while-statement |
   | Breaking loops | if (input == "done") break; | https://learn.microsoft.com/dotnet/csharp/language-reference/statements/jump-statements |
   | Lowercasing | input.ToLowerInvariant() | https://learn.microsoft.com/dotnet/api/system.string.tolowerinvariant |

3. **Adventure Story / Problem**
   The swamp issues mud sarcasm levels one line at a time. When the sensor prints done, it means the mud is too bored to continue. Debugsworth wants a trimmed log for the night's report.

   Create a console app that:
   - Repeatedly reads lines until done (case-insensitive) appears.
   - Counts how many numeric readings were recorded (use int.TryParse). Non-numeric lines should be ignored with a short note like Ignored: frogs croaked.
   - After the loop, print Valid readings: X.

4. **Example Input/Output**
   Input:
   `
   5
   frogs
   2
   DONE
   `

   Output:
   `
   Ignored: frogs croaked
   Valid readings: 2
   `

5. **Tone Reminder**
   Imagine filtering gossip in a swampy group chat—light sarcasm, high focus.