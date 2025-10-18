1. **Purpose**
   Catch specific exceptions when parsing swamp invoices.

2. **Recipe List**
   | Concept | Example | Reference |
   | --- | --- | --- |
   | 	ry/catch | 	ry { ... } catch (FormatException ex) | https://learn.microsoft.com/dotnet/csharp/language-reference/statements/try-catch |
   | Throwing exceptions | 	hrow new InvalidOperationException("..." ); | https://learn.microsoft.com/dotnet/csharp/language-reference/keywords/throw |
   | inally block | inally { CleanUp(); } | https://learn.microsoft.com/dotnet/csharp/language-reference/statements/try-finally |

3. **Adventure Story / Problem**
   The swamp finance office sends invoices scribbled in algae. You must parse them carefully and report back without crashing the console.

   Build a console app that:
   - Reads an invoice line mount|description.
   - Throws a custom InvalidInvoiceException if the amount cannot parse as decimal.
   - Catches InvalidInvoiceException to print Invoice error: message.
   - In inally, always print Ledger updated.
   - On success, print Processed amount X for description.

4. **Example Input/Output**
   Input:
   `
   25.50|Snack subsidy
   `

   Output:
   `
   Processed amount 25.50 for Snack subsidy
   Ledger updated.
   `

5. **Tone Reminder**
   Speak like a calm accountant soothing nervous frogs while balancing books.