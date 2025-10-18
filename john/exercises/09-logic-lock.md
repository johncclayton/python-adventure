1. **Purpose** – New concept: combine booleans with `&&`, `||`, and `!`.
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| Logical operators | `bool ready = hasMap && !isLost;` | [Logical operators](https://learn.microsoft.com/dotnet/csharp/language-reference/operators/boolean-logical-operators) |

3. **Adventure Story / Problem** – At the swamp checkpoint, a lock opens only when the guard sees proof John knows how to combine readiness signals. Create two boolean indicators—one for map possession and one for gumboot status. Use logical operators to determine if the party can cross, then print the result.

4. **Example Input/Output**

```
Output
Crossing ready? True
```
