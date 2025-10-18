1. **Purpose** – New concept: ensure cleanup with the `using` statement.
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| using statement | `using var reader = new StringReader(...);` | [using statement](https://learn.microsoft.com/dotnet/csharp/language-reference/statements/using) |

3. **Adventure Story / Problem** – A librarian mermaid hands out soggy parchment but requires proof that John disposes of magical readers responsibly. Use a `using` declaration with `StringReader` to consume two lines of text and print them.

4. **Example Input/Output**

```
Output
First line: Labyrinth logs
Second line: Swamp minutes
```
