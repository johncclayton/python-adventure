1. **Purpose** – New concept: declare and invoke a custom delegate type.
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| Custom delegate | `public delegate string Chant(string name);` | [Custom delegate](https://learn.microsoft.com/dotnet/csharp/programming-guide/delegates/) |

3. **Adventure Story / Problem** – A rune drum only responds when a delegate is declared to route chants precisely through its echo chambers. Declare a delegate that takes a string and returns a string. Instantiate it with a lambda that formats a chant, then invoke and print the result.

4. **Example Input/Output**

```
Output
Chanting: Rise, Debugsworth!
```
