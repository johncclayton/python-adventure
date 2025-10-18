1. **Purpose** – New concept: combine enum flags with bitwise OR.
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| [Flags] enum | `LabGear pack = LabGear.Map | LabGear.Lantern;` | [[Flags] enum](https://learn.microsoft.com/dotnet/api/system.flagsattribute) |

3. **Adventure Story / Problem** – Festival ushers only admit adventurers who pack multiple gear flags and can read them back with pride. Create a `[Flags]` enum for gear items, combine two flags, and print the composite pack.

4. **Example Input/Output**

```
Output
Pack includes: Lantern, Boots
```
