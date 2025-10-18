1. **Purpose**
   Enforce immutability in a struct to keep enchanted snack coupons from mutating.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | eadonly struct | public readonly struct Coupon | https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/struct |
   | init accessor | public int Uses { get; init; } | https://learn.microsoft.com/dotnet/csharp/language-reference/proposals/csharp-9.0/init |
   | Copy with modification | ar next = coupon with { Uses = 0 }; | https://learn.microsoft.com/dotnet/csharp/fundamentals/types/records#nondestructive-mutation | 

3. **Adventure Story / Problem**
   The swamp snack bar issues coupons that are valid only once per quest step. Build a struct that guards each coupon's state.

   Requirements:
   - Define a eadonly struct SnackCoupon with properties Code, UsesRemaining, and Value (decimal).
   - Provide a constructor assigning all properties.
   - Implement a method Redeem() returning a new SnackCoupon with UsesRemaining - 1 but never below zero.
   - Demonstrate in Main that redeeming a coupon returns a new value while the original remains unchanged.

4. **Example Input/Output**
   Input: *(none)*

   Output:
   `
   Before: CRUNCH-7 -> Uses 2
   After: CRUNCH-7 -> Uses 1
   `

5. **Tone Reminder**
   Speak like a meticulous swamp accountant guarding every crunchy credit.