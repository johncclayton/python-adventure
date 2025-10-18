1. **Purpose** – New concept: serialize data with `JsonSerializer`.
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| JSON serialize | `JsonSerializer.Serialize(data);` | [JSON serialize](https://learn.microsoft.com/dotnet/standard/serialization/system-text-json-overview) |

3. **Adventure Story / Problem** – A bureaucratic crab requires that meeting notes be packaged as JSON before stamping them with approval. Create a simple class with two properties, instantiate it, serialize it to JSON, and print the JSON string.

4. **Example Input/Output**

```
Output
{"Hero":"John","Status":"Prepared"}
```
