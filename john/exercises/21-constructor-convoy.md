1. **Purpose** – New concept: wire up a constructor to require starting data.
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| Class constructor | `public Caravan(string leader) { Leader = leader; }` | [Class constructor](https://learn.microsoft.com/dotnet/csharp/programming-guide/classes-and-structs/constructors) |

3. **Adventure Story / Problem** – The caravan gate opens only for classes that arrive fully initialized. Write a class whose constructor accepts a leader name and wagon count, stores them in read-only properties, then print those properties.

4. **Example Input/Output**

```
Output
Leader: Debugsworth
Wagons: 2
```
