1. **Purpose** – New concept: catch exceptions with `try`/`catch`.
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| try/catch | `try { ... } catch (FormatException) { ... }` | [try/catch](https://learn.microsoft.com/dotnet/csharp/language-reference/statements/exception-handling-statements) |

3. **Adventure Story / Problem** – An annoyed swamp accountant tosses random scroll inputs. John must guard against bad formats gracefully. Wrap an `int.Parse` call in a `try/catch`. Print a success message or a fallback line when parsing fails.

4. **Example Input/Output**

```
Output
Parse failed: invalid rune number.
```
