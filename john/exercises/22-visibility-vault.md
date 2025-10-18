1. **Purpose** – New concept: safeguard fields with access modifiers.
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| Access modifiers | `private readonly string _secret;` | [Access modifiers](https://learn.microsoft.com/dotnet/csharp/programming-guide/classes-and-structs/access-modifiers) |

3. **Adventure Story / Problem** – A vault imp inspects John's class design to ensure secrets stay private while public methods share only what's needed. Create a class with a private field storing a password and a public method that returns a formatted reveal message. Instantiate and print that message.

4. **Example Input/Output**

```
Output
Vault whispers: frog-harmony
```
