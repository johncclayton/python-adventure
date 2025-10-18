1. **Purpose** – Show Joshua how `bool()` judges truthiness so he can predict which stats trigger the trapdoor treadmill.
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| Evaluate truthiness with bool() | `bool(value)` | [Evaluate truthiness with bool()](https://docs.python.org/3/library/functions.html#bool) |

3. **Adventure Story / Problem** – Coach Flexadecimal installed a trapdoor treadmill under the chickens. It activates whenever a falsy value arrives. Joshua must test a trio of stats before stepping on it. Create three variables: an empty string, a list with one dumbbell weight, and zero. Print each value with `bool(value)` so Joshua knows which ones count as truthy.

4. **Example Input/Output**

```
Output
Empty Chant -> False
Single Plate -> True
Zero Hops -> False
```
