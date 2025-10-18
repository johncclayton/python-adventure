1. **Purpose**
   Transform data with LINQ `Select` and anonymous types to plan swamp snacks.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | Anonymous type | `var snack = new { Name = "Chips", Calories = 120 };` | https://learn.microsoft.com/dotnet/csharp/programming-guide/classes-and-structs/anonymous-types |
   | LINQ `.Select` projection | `items.Select(i => new { i.Name, i.Cost * 2 })` | https://learn.microsoft.com/dotnet/csharp/programming-guide/concepts/linq/projection-operations |
   | Ordering results | `.OrderBy(x => x.Calories)` | https://learn.microsoft.com/dotnet/api/system.linq.enumerable.orderby |

3. **Adventure Story / Problem**
   The snack committee wants calorie-adjusted menu cards sorted from lightest to heaviest.

   Build a console app that:
   - Defines a list of snack tuples `(name, calories)`.
   - Uses LINQ to project into anonymous types containing the name, calories, and a string `Mood` set to `"Featherlight"` if under 150 calories else `"Hearty"`.
   - Order the projections by calories and print lines `Name: Mood (calories)`.

4. **Example Input/Output**
   Input: *(none)*

   Output:
   ```
   Glow Popcorn: Featherlight (90)
   Mud Pie Bites: Hearty (220)
   ```

5. **Tone Reminder**
   Deliver menu commentary like a cheerful gala announcer.