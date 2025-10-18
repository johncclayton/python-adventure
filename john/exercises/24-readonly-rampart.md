1. **Purpose** – New concept: prevent mutation with a `readonly struct`.
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| readonly struct | `readonly struct RuneVector { ... }` | [readonly struct](https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/struct#readonly-struct) |

3. **Adventure Story / Problem** – Rampart guardians require vectors that never shift once drawn, otherwise the walls wobble. Define a `readonly struct` with two get-only properties and a constructor. Instantiate it and print the components.

4. **Example Input/Output**

```
Output
Vector row: 1
Vector column: -1
```
