1. **Purpose** – New concept: craft a `switch` expression with `when` guards.
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| switch expression with when | `var plan = wind switch { int level when level > 10 => ... };` | [switch expression with when](https://learn.microsoft.com/dotnet/csharp/language-reference/operators/switch-expression) |

3. **Adventure Story / Problem** – In the undersea meeting room, a jellyfish agenda board only approves strategies chosen via switch mosaics that consider the current currents. Store an integer current speed. Use a `switch` expression with `when` clauses to produce a string plan for fast, breezy, or calm water, then print it.

4. **Example Input/Output**

```
Output
Strategy: anchor the chairs.
```
