1. **Purpose** – New concept: order specific catches before general ones.
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| Catch ordering | `catch (InvalidOperationException) { } catch (Exception) { }` | [Catch ordering](https://learn.microsoft.com/dotnet/csharp/fundamentals/exceptions/) |

3. **Adventure Story / Problem** – A sarcastic vine tests whether John handles precise grievances before generic grumbles. Throw an `InvalidOperationException` inside a `try` block, catch it specifically, then fall back to a general `Exception` catch that would run otherwise. Print which catch triggered.

4. **Example Input/Output**

```
Output
Handled specific swamp hiccup.
```
