1. **Purpose** – New concept: express a method body with the `=>` expression-bodied syntax.
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| Expression-bodied method | `static string Chant(int beat) => $"Beat {beat}";` | [Expression-bodied method](https://learn.microsoft.com/dotnet/csharp/programming-guide/statements-expressions-operators/expression-bodied-members) |

3. **Adventure Story / Problem** – The labyrinth metronome only syncs with concise arrow-formed chants. Write a helper method using expression-bodied syntax that formats a beat number. Call it twice and print both results.

4. **Example Input/Output**

```
Output
Beat 1 steady
Beat 2 steady
```
