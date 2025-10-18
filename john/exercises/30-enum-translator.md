1. **Purpose** – New concept: convert enums to and from strings/ints.
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| Enum conversion | `Enum.Parse<BiomeMood>("Snarky");` | [Enum conversion](https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/enum#conversions) |

3. **Adventure Story / Problem** – A bureaucratic eel demands mood paperwork in every format—numeric, text, and enum. Pick an enum value, cast it to `int`, parse a string back to the enum, then print both results.

4. **Example Input/Output**

```
Output
Numeric mood: 1
Parsed mood: Snarky
```
