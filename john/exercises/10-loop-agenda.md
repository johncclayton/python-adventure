1. **Purpose**
   Traverse collections with oreach to rehearse the eel-led agenda.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | Array initialization | string[] topics = { "Torches", "Snacks" }; | https://learn.microsoft.com/dotnet/csharp/programming-guide/arrays/single-dimensional-arrays |
   | oreach loop | oreach (var topic in topics) | https://learn.microsoft.com/dotnet/csharp/language-reference/statements/iteration-statements#the-foreach-statement |
   | String interpolation | $"Topic: {topic}" | https://learn.microsoft.com/dotnet/csharp/language-reference/tokens/interpolated |

3. **Adventure Story / Problem**
   In the Undersea World of Unexpected Meetings, a drifting boardroom asks Debugsworth to present the meeting topics with gusto. Each topic must earn a whimsical tagline.

   Build a console app that:
   - Declares an array of three agenda topics.
   - Uses oreach to print Topic: {topic} -> {tagline} for each.
   - After looping, print Agenda bubbles delivered.

4. **Example Input/Output**
   Input: *(none)*

   Output:
   `
   Topic: Torches -> infused with glowfish glitter
   Topic: Snacks -> ethically sourced swamp chips
   Topic: Exit Strategies -> involving polite eels
   Agenda bubbles delivered.
   `

5. **Tone Reminder**
   Embrace your inner undersea emcee—bubbly, charming, and a touch ridiculous.