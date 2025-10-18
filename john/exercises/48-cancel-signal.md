1. **Purpose** – New concept: respond to a `CancellationToken` in async work.
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| CancellationToken | `token.ThrowIfCancellationRequested();` | [CancellationToken](https://learn.microsoft.com/dotnet/standard/threading/cancellation) |

3. **Adventure Story / Problem** – A kelp project manager practices humane meetings: every async scan must halt the moment someone waves the cancel flag. Create a method that accepts a `CancellationToken`, checks it, and prints whether the scan completed or was canceled. Trigger cancellation before awaiting the task to prove it respects the token.

4. **Example Input/Output**

```
Output
Scan canceled politely.
```
