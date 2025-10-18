1. **Purpose** – New concept: adjust data via a `ref` parameter.
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| ref parameter | `Refill(ref torches);` | [ref parameter](https://learn.microsoft.com/dotnet/csharp/language-reference/keywords/ref) |

3. **Adventure Story / Problem** – A supply gnome only tops up torches if John proves he can hand the counter a reference so the value updates in place. Create an integer torch count, pass it by `ref` to a helper that adds 2, then print the new count.

4. **Example Input/Output**

```
Output
Torches after refill: 5
```
