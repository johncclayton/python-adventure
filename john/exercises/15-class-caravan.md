1. **Purpose**
   Explore constructor overloading and chaining to set up companion transport plans.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | Constructor overload | public Caravan(string name) | https://learn.microsoft.com/dotnet/csharp/programming-guide/classes-and-structs/constructors |
   | Constructor chaining | : this(name, "foot") | https://learn.microsoft.com/dotnet/csharp/language-reference/keywords/this#constructor-qualifiers |
   | Default parameter values | public Caravan(string name, string mode = "foot") | https://learn.microsoft.com/dotnet/csharp/language-reference/parameters/default-arguments |

3. **Adventure Story / Problem**
   The caravan master insists every companion has a travel plan before leaving the gate. Some ride eels, others prefer teleporting chuck wagons.

   Build a TravelPlan class with:
   - Two constructors: one taking only 
ame and chaining to a second that accepts mode and departureHour (int).
   - Auto-properties for Name, Mode, and DepartureHour.
   - ToSummary() method that returns "Name via Mode at HH:00".
   - In Main, create plans using each constructor and print their summaries.

4. **Example Input/Output**
   Input: *(none)*

   Output:
   `
   Bard via echo-wagon at 19:00
   Barbarian via eelback at 21:00
   `

5. **Tone Reminder**
   Announce departures like a whimsical train conductor—clarity with a wink.