1. **Purpose**
   Grow and shrink a List<T> while tracking volunteer morale levels.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | List creation | ar list = new List<int>(); | https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1 |
   | Add/Remove | list.Add(5); list.Remove(5); | https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1.add |
   | Looping with index | or (int i = 0; i < list.Count; i++) | https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1.count |

3. **Adventure Story / Problem**
   During a morale check, Debugsworth collects cheer scores from volunteers. Anyone scoring below 3 must be reassigned to snack duty.

   Build a console app that:
   - Reads cheer scores until a blank line.
   - Stores them in a List<int>.
   - Removes every score below 3.
   - Prints the remaining scores with indexes, then prints the average morale (rounded to one decimal using Math.Round).

4. **Example Input/Output**
   Input:
   `
   5
   2
   4

   `

   Output:
   `
   Slot 0: 5
   Slot 1: 4
   Average morale: 4.5
   `

5. **Tone Reminder**
   Sound like an upbeat coach who gracefully redirects low morale toward pastry duty.