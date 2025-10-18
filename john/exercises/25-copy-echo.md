1. **Purpose** – New concept: observe value-copy behavior with structs.
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| Struct copy semantics | `var copy = original;` | [Struct copy semantics](https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/struct#value-type-semantics) |

3. **Adventure Story / Problem** – Echo goblins test whether John knows struct copies are separate echoes, not shared echoes like classes. Create a struct with a mutable property. Copy it to another variable, change the copy, then print both to show the original stayed the same.

4. **Example Input/Output**

```
Output
Original charge: 10
Copied charge: 5
```
