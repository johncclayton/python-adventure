1. **Purpose** – New concept: implement multiple interfaces on one class.
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| Multiple interfaces | `class Mimic : IChant, IAlarm` | [Multiple interfaces](https://learn.microsoft.com/dotnet/csharp/programming-guide/interfaces/explicit-interface-implementation) |

3. **Adventure Story / Problem** – A shape-shifting mimic offers contracts only if John can juggle several interface obligations at once. Create two interfaces with different methods and a class implementing both. Use each interface reference to call its respective method and print the messages.

4. **Example Input/Output**

```
Output
Report: Mood stable
Alarm: Confetti deployed
```
