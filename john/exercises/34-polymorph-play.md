1. **Purpose** – New concept: invoke polymorphic behavior through interface references.
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| Polymorphism | `foreach (var actor in troupe) actor.Perform();` | [Polymorphism](https://learn.microsoft.com/dotnet/csharp/fundamentals/object-oriented/polymorphism) |

3. **Adventure Story / Problem** – An undersea improv troupe only performs when the audience can treat every actor as the same contract while letting each improvise wildly. Populate a list of performers implementing the same interface. Loop over the list calling the shared method, printing each unique result.

4. **Example Input/Output**

```
Output
Performance: Bard strums wifi blues
Performance: Goblin beatboxes bug fixes
```
