1. **Purpose** – New concept: project data with LINQ `Select`.
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| LINQ Select | `var chants = beats.Select(b => $"Beat {b}");` | [LINQ Select](https://learn.microsoft.com/dotnet/api/system.linq.enumerable.select) |

3. **Adventure Story / Problem** – A rhythm octopus wants every beat turned into a chant string using LINQ instead of manual loops. Start with an integer array of beat numbers. Use `Select` to create strings like `Beat 1 ready`. Print each transformed chant.

4. **Example Input/Output**

```
Output
Beat 1 ready
Beat 2 ready
Beat 3 ready
```
