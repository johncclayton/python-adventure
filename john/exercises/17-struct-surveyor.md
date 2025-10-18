1. **Purpose**
   Compare structs and classes by modeling lightweight maze coordinates.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | Struct declaration | public readonly struct MazePoint | https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/struct |
   | eadonly members | public readonly int X; | https://learn.microsoft.com/dotnet/csharp/language-reference/keywords/readonly |
   | Value copy semantics | ar copy = original; copy.X | https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/struct#value-type-behavior |

3. **Adventure Story / Problem**
   The maze cartographer needs precise coordinates stamped on parchment without reference-sharing mishaps. You're tasked with designing the coordinate struct.

   Build a console app that:
   - Declares a eadonly struct MazePoint with properties X, Y, and method WithOffset(int dx, int dy) returning a new MazePoint.
   - In Main, instantiate one point, create an offset copy, and print both to show the original remains unchanged.

4. **Example Input/Output**
   Input: *(none)*

   Output:
   `
   Original: (2, 5)
   Offset: (5, 9)
   `

5. **Tone Reminder**
   Channel a precise surveyor—calm, confident, and a little proud of those crisp coordinates.