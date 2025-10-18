# C# Quest Outline for John

## Act I: Foundations & Syntax
1. Getting Started: install .NET SDK; scaffold a console app with `dotnet new console`; execute and rebuild with `dotnet run`.
2. Types & Variables: declare primitives (`int`, `double`, `bool`); apply `var` with compiler inference; interpolate strings using `$"value {x}"`.
3. Operators & Expressions: perform arithmetic `+ - * / %`; compare values with `== != < >`; combine conditions using `&& || !`.
4. Control Flow: branch with `if/else` and chained `else if`; express decisions via `switch` expressions with `when` guards; iterate using `for`, `while`, and `foreach`.
5. Methods: define `static` and instance methods with signatures; pass parameters by value vs `ref`/`out`; write expression-bodied members with `=>`.

## Act II: Data Structures & Object Modeling
1. Classes & Objects: declare classes with fields and auto-properties; instantiate objects with constructors; manage visibility using `public`, `internal`, `private`.
2. Structs vs Classes: create `struct` for lightweight value types; enforce immutability with `readonly` members; observe copy vs reference semantics.
3. Collections: manipulate arrays `T[]` for fixed sequences; grow lists with `List<T>.Add`/`Remove`; map keys to values via `Dictionary<TKey, TValue>`.
4. Enums & Flags: define enums with explicit integral values; convert between enum and string/int; combine options using `[Flags]` and bitwise ops.
5. Interfaces & Polymorphism: declare interfaces describing contracts; implement multiple interfaces on a class; invoke polymorphic behavior through base/interface references.

## Act III: Robust C# Habits
1. Error Handling: wrap risky code in `try/catch`; catch specific exception types before general; ensure cleanup using `finally` or `using`.
2. LINQ Fundamentals: filter collections with `.Where`; transform results using `.Select` and anonymous types; aggregate with `.OrderBy`/`.Sum`.
3. Files & Data: read text using `File.ReadAllLines`; serialize/deserialise JSON via `JsonSerializer`; handle file resources with `using` statements.
4. Delegates & Events: declare custom delegate signatures; employ `Action`/`Func` with lambda expressions; raise and subscribe to events via the `event` keyword.
5. Async Basics: create asynchronous methods returning `Task`; await I/O-bound calls with `await`; respond to cancellation using `CancellationToken`.

## Act IV: Crafting Larger Adventures
1. Organizing Projects: structure namespaces matching folders; manage multi-project solutions with `dotnet new sln`/`dotnet sln add`; share code through project references.
2. Dependency Injection: configure a host with `Host.CreateDefaultBuilder`; register services using `AddSingleton`/`AddScoped`/`AddTransient`; request dependencies through constructor injection.
3. Testing & Debugging: write xUnit tests with `[Fact]`; follow arrange-act-assert layout; inspect runtime state via breakpoints and watches in the debugger.
4. Performance Awareness: benchmark code with `BenchmarkDotNet`; limit allocations using `Span<T>`/`Memory<T>`; choose value vs reference types for hot paths.
5. Packaging & Sharing: consume packages with `dotnet add package`; pack libraries using `dotnet pack`; publish artifacts using `dotnet nuget push`.

## Optional Epilogue Topics
1. Advanced Pattern Matching: apply relational patterns (`>`, `<`); combine logical patterns with `and`, `or`, `not`; destructure nested types using recursive patterns.
2. Records & with-expressions: declare `record` types for immutable models; use positional records for concise constructors; clone with modified values via `with`.
3. Unsafe & Span Adventures: slice buffers using `Span<T>` and `ReadOnlySpan<T>`; allocate stack memory with `stackalloc`; interop with pointers inside an `unsafe` block.
4. Interop & Scripting: call native functions using `DllImport`; leverage `dynamic` for late binding; host C# scripts through `CSharpScript.EvaluateAsync`.
