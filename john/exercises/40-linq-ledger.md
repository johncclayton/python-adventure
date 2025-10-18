1. **Purpose** – New concept: order and aggregate with LINQ `OrderBy` and `Sum`.
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| LINQ OrderBy + Sum | `int total = loot.OrderBy(x => x).Sum();` | [LINQ OrderBy + Sum](https://learn.microsoft.com/dotnet/api/system.linq.enumerable.orderby) |

3. **Adventure Story / Problem** – The ledger kraken insists that loot is sorted and tallied in elegant fluent style. Create an array of treasure values, order them ascending, compute the sum, and print both the sorted list and total.

4. **Example Input/Output**

```
Output
Sorted loot: 1, 3, 5
Total sparkle: 9
```
