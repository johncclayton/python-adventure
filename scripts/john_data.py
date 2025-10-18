EXERCISES = [
    {
        "number": "01",
        "slug": "spark-console",
        "purpose": "New concept: scaffold a fresh console project with `dotnet new console`.",
        "concept": "Scaffold console app",
        "syntax": "dotnet new console -o MazeBeacon",
        "docs": "https://learn.microsoft.com/dotnet/core/tools/dotnet-new",
        "story": (
            "Sir Johnathan Debugsworth finds a rune-locked kiosk in the Labyrinth of Patchy Wi-Fi. "
            "It only opens for heroes who conjure a fresh console project template to prove they travel with a clean codebase."
        ),
        "task": (
            "Use `dotnet new console -n MazeBeacon` to create a project. In `Program.cs`, print a single line "
            "confirming the beacon is online."
        ),
        "example": "Output\nMaze beacon scaffold complete!",
        "solution": "Console.WriteLine(\"Maze beacon scaffold complete!\");",
    },
    {
        "number": "02",
        "slug": "run-ritual",
        "purpose": "New concept: execute the console quest with `dotnet run`.",
        "concept": "Run console app",
        "syntax": "dotnet run",
        "docs": "https://learn.microsoft.com/dotnet/core/tools/dotnet-run",
        "story": (
            "The kiosk boots but demands proof that John can launch spells on demand. "
            "A snarky swamp frog insists that only code triggered with `dotnet run` counts toward swamp entry."
        ),
        "task": (
            "Inside the project, print two status lines that make it obvious the chant came from an executed app. "
            "Run it with `dotnet run` to appease the frog."
        ),
        "example": "Output\nExecuting labyrinth link...\nRouter spirit answered!",
        "solution": "Console.WriteLine(\"Executing labyrinth link...\");\nConsole.WriteLine(\"Router spirit answered!\");",
    },
    {
        "number": "03",
        "slug": "numeric-ledger",
        "purpose": "New concept: declare numeric primitives (`int` and `double`).",
        "concept": "Declare numeric variables",
        "syntax": "int corridorTurns = 12;",
        "docs": "https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/numeric-types",
        "story": (
            "Before entering the maze, John scribbles a corridor ledger. The kiosk only waves him through if the "
            "log clearly separates whole-number turns from fractional torch power."
        ),
        "task": (
            "Create an `int` variable for turns and a `double` for torch power. Print each value on its own line so the ledger is neat."
        ),
        "example": "Output\n12\n3.5",
        "solution": "int corridorTurns = 12;\ndouble torchPower = 3.5;\nConsole.WriteLine(corridorTurns);\nConsole.WriteLine(torchPower);",
    },
    {
        "number": "04",
        "slug": "boolean-beacon",
        "purpose": "New concept: store quest state in a `bool`.",
        "concept": "Boolean variable",
        "syntax": "bool beaconLit = true;",
        "docs": "https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/bool",
        "story": (
            "A labyrinth gargoyle refuses to report signal strength unless John tracks whether the Wi-Fi torch is lit. "
            "The statue loves `true`/`false` more than riddles."
        ),
        "task": (
            "Create a `bool` indicating whether the signal torch is active and print a friendly message that includes the value."
        ),
        "example": "Output\nSignal torch lit? True",
        "solution": "bool signalTorchLit = true;\nConsole.Write(\"Signal torch lit? \");\nConsole.WriteLine(signalTorchLit);",
    },
    {
        "number": "05",
        "slug": "var-scout",
        "purpose": "New concept: let the compiler infer types with `var`.",
        "concept": "Type inference with var",
        "syntax": "var swampNotes = \"Bring boots\";",
        "docs": "https://learn.microsoft.com/dotnet/csharp/language-reference/keywords/var",
        "story": (
            "At the swamp gate, an eel librarian slides a form across the mud. It only accepts entries written with the mysterious `var` ink."
        ),
        "task": (
            "Declare two variables using `var`—one string message and one integer count. Print both to show the eel the compiler guessed correctly."
        ),
        "example": "Output\nVar note: Bring boots\nVar count: 3",
        "solution": "var swampMessage = \"Bring boots\";\nvar swampGuardCount = 3;\nConsole.WriteLine($\"Var note: {swampMessage}\");\nConsole.WriteLine($\"Var count: {swampGuardCount}\");",
    },
    {
        "number": "06",
        "slug": "string-sigil",
        "purpose": "New concept: weave values into text with string interpolation.",
        "concept": "String interpolation",
        "syntax": "$\"Guide {hero} holds {torches} torches\"",
        "docs": "https://learn.microsoft.com/dotnet/csharp/language-reference/tokens/interpolated",
        "story": (
            "The labyrinth hall monitor demands an interpolated sigil that names the hero and torch count in a single flourish."
        ),
        "task": (
            "Use string interpolation to print one sentence mentioning the hero name and number of torches being carried."
        ),
        "example": "Output\nSir Debugsworth carries 3 torches through the maze.",
        "solution": "string hero = \"Sir Debugsworth\";\nint torches = 3;\nConsole.WriteLine($\"{hero} carries {torches} torches through the maze.\");",
    },
    {
        "number": "07",
        "slug": "arithmetic-forge",
        "purpose": "New concept: combine values with arithmetic operators (`+`, `-`, `*`, `/`, `%`).",
        "concept": "Arithmetic operators",
        "syntax": "int total = baseRunes + bonusRunes;",
        "docs": "https://learn.microsoft.com/dotnet/csharp/language-reference/operators/arithmetic-operators",
        "story": (
            "A forge sprite tallies rune fragments. It insists John prove he can add, subtract, multiply, divide, and find remainders before handing over upgrade parts."
        ),
        "task": (
            "Start with two integers for runes collected and lost. Compute a repaired count, a doubled batch, and the remainder when split between two goblins. Print the three results."
        ),
        "example": "Output\nRepaired: 8\nDoubled: 18\nSplit remainder: 1",
        "solution": "int collected = 10;\nint lost = 2;\nint repaired = collected - lost;\nint doubled = repaired * 2;\nint remainder = doubled % 2;\nConsole.WriteLine($\"Repaired: {repaired}\");\nConsole.WriteLine($\"Doubled: {doubled}\");\nConsole.WriteLine($\"Split remainder: {remainder}\");",
    },
    {
        "number": "08",
        "slug": "compare-compass",
        "purpose": "New concept: compare values with relational operators to produce booleans.",
        "concept": "Comparison operators",
        "syntax": "bool isCalm = slimeLevel < 5;",
        "docs": "https://learn.microsoft.com/dotnet/csharp/language-reference/operators/comparison-operators",
        "story": (
            "The swamp issues a comparison compass that glows only when John checks if slime is below danger levels."
        ),
        "task": (
            "Store a slime level and a safety threshold. Compare them with `>` or `<`, assign the result to a `bool`, and print the answer."
        ),
        "example": "Output\nIs slime manageable? True",
        "solution": "int slimeLevel = 2;\nint safeThreshold = 4;\nbool isManageable = slimeLevel < safeThreshold;\nConsole.WriteLine($\"Is slime manageable? {isManageable}\");",
    },
    {
        "number": "09",
        "slug": "logic-lock",
        "purpose": "New concept: combine booleans with `&&`, `||`, and `!`.",
        "concept": "Logical operators",
        "syntax": "bool ready = hasMap && !isLost;",
        "docs": "https://learn.microsoft.com/dotnet/csharp/language-reference/operators/boolean-logical-operators",
        "story": (
            "At the swamp checkpoint, a lock opens only when the guard sees proof John knows how to combine readiness signals."
        ),
        "task": (
            "Create two boolean indicators—one for map possession and one for gumboot status. Use logical operators to determine if the party can cross, then print the result."
        ),
        "example": "Output\nCrossing ready? True",
        "solution": "bool hasMap = true;\nbool wearingBoots = false;\nbool readyToCross = hasMap && !wearingBoots || wearingBoots;\nConsole.WriteLine($\"Crossing ready? {readyToCross}\");",
    },
    {
        "number": "10",
        "slug": "if-bridge",
        "purpose": "New concept: branch with `if`/`else`.",
        "concept": "if/else statement",
        "syntax": "if (noiseLevel > 5) { ... } else { ... }",
        "docs": "https://learn.microsoft.com/dotnet/csharp/language-reference/statements/selection-statements#the-if-statement",
        "story": (
            "A rickety bridge listens for polite decision making. John must whisper whether to tiptoe or stomp based on the swamp's sarcasm level."
        ),
        "task": (
            "Store a sarcasm score. If it's above 5, print a warning; otherwise print that the path is clear."
        ),
        "example": "Output\nBridge protocol: tiptoe softly.",
        "solution": "int sarcasmScore = 7;\nif (sarcasmScore > 5)\n{\n    Console.WriteLine(\"Bridge protocol: tiptoe softly.\");\n}\nelse\n{\n    Console.WriteLine(\"Bridge protocol: stomp with confidence.\");\n}",
    },
    {
        "number": "11",
        "slug": "elif-fork",
        "purpose": "New concept: extend decisions with `else if` chains.",
        "concept": "else-if chain",
        "syntax": "if (...) { } else if (...) { } else { }",
        "docs": "https://learn.microsoft.com/dotnet/csharp/language-reference/statements/selection-statements#the-if-statement",
        "story": (
            "Three singing frogs share a fork in the swamp. Each croaks a different tune depending on the humidity tier John reports."
        ),
        "task": (
            "Read a humidity level variable and use an `if/else if/else` chain to print one of three travel tips."
        ),
        "example": "Output\nTip: deploy umbrella fins.",
        "solution": "int humidity = 8;\nif (humidity < 3)\n{\n    Console.WriteLine(\"Tip: carry chalk dust.\");\n}\nelse if (humidity < 7)\n{\n    Console.WriteLine(\"Tip: keep maps in plastic wraps.\");\n}\nelse\n{\n    Console.WriteLine(\"Tip: deploy umbrella fins.\");\n}",
    },
    {
        "number": "12",
        "slug": "switch-mosaic",
        "purpose": "New concept: craft a `switch` expression with `when` guards.",
        "concept": "switch expression with when",
        "syntax": "var plan = wind switch { int level when level > 10 => ... };",
        "docs": "https://learn.microsoft.com/dotnet/csharp/language-reference/operators/switch-expression",
        "story": (
            "In the undersea meeting room, a jellyfish agenda board only approves strategies chosen via switch mosaics that consider the current currents."
        ),
        "task": (
            "Store an integer current speed. Use a `switch` expression with `when` clauses to produce a string plan for fast, breezy, or calm water, then print it."
        ),
        "example": "Output\nStrategy: anchor the chairs.",
        "solution": "int currentSpeed = 12;\nstring strategy = currentSpeed switch\n{\n    int level when level > 10 => \"Strategy: anchor the chairs.\",\n    int level when level > 5 => \"Strategy: hand out snorkels.\",\n    _ => \"Strategy: serve tea slowly.\"\n};\nConsole.WriteLine(strategy);",
    },
    {
        "number": "13",
        "slug": "for-baton",
        "purpose": "New concept: repeat actions with a `for` loop.",
        "concept": "for loop",
        "syntax": "for (int step = 1; step <= 3; step++)",
        "docs": "https://learn.microsoft.com/dotnet/csharp/language-reference/statements/iteration-statements#the-for-statement",
        "story": (
            "A drumline of enchanted barrels blocks the path. They only roll aside if John beats the rhythm exactly three times with a marching loop."
        ),
        "task": (
            "Use a `for` loop to print steps 1 through 3 with encouraging text."
        ),
        "example": "Output\nStep 1: left foot\nStep 2: right foot\nStep 3: spin!",
        "solution": "for (int step = 1; step <= 3; step++)\n{\n    Console.WriteLine($\"Step {step}: stay on beat!\");\n}",
    },
    {
        "number": "14",
        "slug": "while-watch",
        "purpose": "New concept: loop until a condition fails with `while`.",
        "concept": "while loop",
        "syntax": "while (bubbleCount > 0) { ... }",
        "docs": "https://learn.microsoft.com/dotnet/csharp/language-reference/statements/iteration-statements#the-while-statement",
        "story": (
            "Bubble couriers float past the meeting reef. John must keep announcing arrivals until the last bubble pops."
        ),
        "task": (
            "Start with a bubble count variable. Use a `while` loop to announce each bubble and decrement the count until zero."
        ),
        "example": "Output\nBubble 3 incoming\nBubble 2 incoming\nBubble 1 incoming",
        "solution": "int bubbleCount = 3;\nwhile (bubbleCount > 0)\n{\n    Console.WriteLine($\"Bubble {bubbleCount} incoming\");\n    bubbleCount--;\n}",
    },
    {
        "number": "15",
        "slug": "foreach-parade",
        "purpose": "New concept: iterate a collection with `foreach`.",
        "concept": "foreach loop",
        "syntax": "foreach (var biome in biomes)",
        "docs": "https://learn.microsoft.com/dotnet/csharp/language-reference/statements/iteration-statements#the-foreach-statement",
        "story": (
            "A parade of biomes demands individual praise. John must salute each location in order without losing track."
        ),
        "task": (
            "Create an array of biome names and use `foreach` to print a cheer for each."
        ),
        "example": "Output\nCheering for Labyrinth\nCheering for Sarcastic Swamp\nCheering for Undersea Meetings",
        "solution": "string[] biomes = { \"Labyrinth\", \"Sarcastic Swamp\", \"Undersea Meetings\" };\nforeach (var biome in biomes)\n{\n    Console.WriteLine($\"Cheering for {biome}\");\n}",
    },
    {
        "number": "16",
        "slug": "static-salute",
        "purpose": "New concept: declare and call a `static` method.",
        "concept": "Static method",
        "syntax": "QuestPlanner.BuildCheer(name);",
        "docs": "https://learn.microsoft.com/dotnet/csharp/programming-guide/classes-and-structs/static-classes-and-static-class-members",
        "story": (
            "A brass automaton salutes only when a proper static fanfare is invoked."
        ),
        "task": (
            "Write a `static` method that accepts a biome name and returns a cheer string. Call it from `Main` (or top level) and print the result."
        ),
        "example": "Output\nFanfare for Labyrinth launched!",
        "solution": "Console.WriteLine(QuestPlanner.BuildCheer(\"Labyrinth\"));\n\nstatic class QuestPlanner\n{\n    public static string BuildCheer(string biome)\n    {\n        return $\"Fanfare for {biome} launched!\";\n    }\n}",
    },
    {
        "number": "17",
        "slug": "instance-inspection",
        "purpose": "New concept: define an instance method and call it on an object.",
        "concept": "Instance method",
        "syntax": "new Torch().Describe();",
        "docs": "https://learn.microsoft.com/dotnet/csharp/programming-guide/classes-and-structs/methods",
        "story": (
            "A torch vendor refuses to hand over flame until an inspector object approves the brightness rating."
        ),
        "task": (
            "Create a class with an instance method `Describe` that returns a sentence. Instantiate the class and print the returned text."
        ),
        "example": "Output\nTorch glow: steady and warm.",
        "solution": "var torch = new TorchInspector();\nConsole.WriteLine(torch.Describe());\n\nclass TorchInspector\n{\n    public string Describe()\n    {\n        return \"Torch glow: steady and warm.\";\n    }\n}",
    },
    {
        "number": "18",
        "slug": "ref-rescue",
        "purpose": "New concept: adjust data via a `ref` parameter.",
        "concept": "ref parameter",
        "syntax": "Refill(ref torches);",
        "docs": "https://learn.microsoft.com/dotnet/csharp/language-reference/keywords/ref",
        "story": (
            "A supply gnome only tops up torches if John proves he can hand the counter a reference so the value updates in place."
        ),
        "task": (
            "Create an integer torch count, pass it by `ref` to a helper that adds 2, then print the new count."
        ),
        "example": "Output\nTorches after refill: 5",
        "solution": "int torches = 3;\nRefill(ref torches);\nConsole.WriteLine($\"Torches after refill: {torches}\");\n\nstatic void Refill(ref int torchCount)\n{\n    torchCount += 2;\n}",
    },
    {
        "number": "19",
        "slug": "expression-arrow",
        "purpose": "New concept: express a method body with the `=>` expression-bodied syntax.",
        "concept": "Expression-bodied method",
        "syntax": "static string Chant(int beat) => $\"Beat {beat}\";",
        "docs": "https://learn.microsoft.com/dotnet/csharp/programming-guide/statements-expressions-operators/expression-bodied-members",
        "story": (
            "The labyrinth metronome only syncs with concise arrow-formed chants."
        ),
        "task": (
            "Write a helper method using expression-bodied syntax that formats a beat number. Call it twice and print both results."
        ),
        "example": "Output\nBeat 1 steady\nBeat 2 steady",
        "solution": "Console.WriteLine(Beat(1));\nConsole.WriteLine(Beat(2));\n\nstatic string Beat(int count) => $\"Beat {count} steady\";",
    },
    {
        "number": "20",
        "slug": "class-quarters",
        "purpose": "New concept: declare auto-properties on a class.",
        "concept": "Auto-implemented properties",
        "syntax": "public string Name { get; set; }",
        "docs": "https://learn.microsoft.com/dotnet/csharp/programming-guide/classes-and-structs/using-properties",
        "story": (
            "A castle steward signs travelers into the hero dormitory only if their class records neatly capture name and courage score."
        ),
        "task": (
            "Create a class with two auto-properties, set them with an object initializer, then print both values."
        ),
        "example": "Output\nRoom: Labyrinth Loft\nCourage: 9",
        "solution": "var room = new HeroQuarters { Name = \"Labyrinth Loft\", CourageScore = 9 };\nConsole.WriteLine($\"Room: {room.Name}\");\nConsole.WriteLine($\"Courage: {room.CourageScore}\");\n\nclass HeroQuarters\n{\n    public string Name { get; set; } = string.Empty;\n    public int CourageScore { get; set; }\n}",
    },
    {
        "number": "21",
        "slug": "constructor-convoy",
        "purpose": "New concept: wire up a constructor to require starting data.",
        "concept": "Class constructor",
        "syntax": "public Caravan(string leader) { Leader = leader; }",
        "docs": "https://learn.microsoft.com/dotnet/csharp/programming-guide/classes-and-structs/constructors",
        "story": (
            "The caravan gate opens only for classes that arrive fully initialized."
        ),
        "task": (
            "Write a class whose constructor accepts a leader name and wagon count, stores them in read-only properties, then print those properties."
        ),
        "example": "Output\nLeader: Debugsworth\nWagons: 2",
        "solution": "var convoy = new Caravan(\"Debugsworth\", 2);\nConsole.WriteLine($\"Leader: {convoy.Leader}\");\nConsole.WriteLine($\"Wagons: {convoy.Wagons}\");\n\nclass Caravan\n{\n    public Caravan(string leader, int wagons)\n    {\n        Leader = leader;\n        Wagons = wagons;\n    }\n\n    public string Leader { get; }\n    public int Wagons { get; }\n}",
    },
    {
        "number": "22",
        "slug": "visibility-vault",
        "purpose": "New concept: safeguard fields with access modifiers.",
        "concept": "Access modifiers",
        "syntax": "private readonly string _secret;",
        "docs": "https://learn.microsoft.com/dotnet/csharp/programming-guide/classes-and-structs/access-modifiers",
        "story": (
            "A vault imp inspects John's class design to ensure secrets stay private while public methods share only what's needed."
        ),
        "task": (
            "Create a class with a private field storing a password and a public method that returns a formatted reveal message. Instantiate and print that message."
        ),
        "example": "Output\nVault whispers: frog-harmony",
        "solution": "var vault = new AccessVault(\"frog-harmony\");\nConsole.WriteLine(vault.Reveal());\n\nclass AccessVault\n{\n    private readonly string _secret;\n\n    public AccessVault(string secret)\n    {\n        _secret = secret;\n    }\n\n    public string Reveal() => $\"Vault whispers: {_secret}\";\n}",
    },
    {
        "number": "23",
        "slug": "struct-sketch",
        "purpose": "New concept: model light data with a `struct`.",
        "concept": "Define struct",
        "syntax": "struct RunePoint { public int Row; }",
        "docs": "https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/struct",
        "story": (
            "A survey sprite insists the map grid is drawn with structs so coordinates stay lean and snappy."
        ),
        "task": (
            "Declare a `struct` representing a rune's row and column. Instantiate it and print both values."
        ),
        "example": "Output\nRune row: 2\nRune column: 5",
        "solution": "var point = new RunePoint(2, 5);\nConsole.WriteLine($\"Rune row: {point.Row}\");\nConsole.WriteLine($\"Rune column: {point.Column}\");\n\nstruct RunePoint\n{\n    public RunePoint(int row, int column)\n    {\n        Row = row;\n        Column = column;\n    }\n\n    public int Row;\n    public int Column;\n}",
    },
    {
        "number": "24",
        "slug": "readonly-rampart",
        "purpose": "New concept: prevent mutation with a `readonly struct`.",
        "concept": "readonly struct",
        "syntax": "readonly struct RuneVector { ... }",
        "docs": "https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/struct#readonly-struct",
        "story": (
            "Rampart guardians require vectors that never shift once drawn, otherwise the walls wobble."
        ),
        "task": (
            "Define a `readonly struct` with two get-only properties and a constructor. Instantiate it and print the components."
        ),
        "example": "Output\nVector row: 1\nVector column: -1",
        "solution": "var vector = new RuneVector(1, -1);\nConsole.WriteLine($\"Vector row: {vector.Row}\");\nConsole.WriteLine($\"Vector column: {vector.Column}\");\n\nreadonly struct RuneVector\n{\n    public RuneVector(int row, int column)\n    {\n        Row = row;\n        Column = column;\n    }\n\n    public int Row { get; }\n    public int Column { get; }\n}",
    },
    {
        "number": "25",
        "slug": "copy-echo",
        "purpose": "New concept: observe value-copy behavior with structs.",
        "concept": "Struct copy semantics",
        "syntax": "var copy = original;",
        "docs": "https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/struct#value-type-semantics",
        "story": (
            "Echo goblins test whether John knows struct copies are separate echoes, not shared echoes like classes."
        ),
        "task": (
            "Create a struct with a mutable property. Copy it to another variable, change the copy, then print both to show the original stayed the same."
        ),
        "example": "Output\nOriginal charge: 10\nCopied charge: 5",
        "solution": "var original = new ChargeRune(10);\nvar copy = original;\ncopy.Power = 5;\nConsole.WriteLine($\"Original charge: {original.Power}\");\nConsole.WriteLine($\"Copied charge: {copy.Power}\");\n\nstruct ChargeRune\n{\n    public ChargeRune(int power)\n    {\n        Power = power;\n    }\n\n    public int Power { get; set; }\n}",
    },
    {
        "number": "26",
        "slug": "array-atlas",
        "purpose": "New concept: organize fixed slots with arrays.",
        "concept": "Array basics",
        "syntax": "string[] portals = { \"Labyrinth\", \"Swamp\" };",
        "docs": "https://learn.microsoft.com/dotnet/csharp/programming-guide/arrays/",
        "story": (
            "A cartographer snail wants proof that John can store portal names in tidy slots before stamping the map."
        ),
        "task": (
            "Declare a string array with three portal names and print the second entry."
        ),
        "example": "Output\nSecond portal: Sarcastic Swamp",
        "solution": "string[] portals = { \"Labyrinth\", \"Sarcastic Swamp\", \"Undersea Meetings\" };\nConsole.WriteLine($\"Second portal: {portals[1]}\");",
    },
    {
        "number": "27",
        "slug": "list-larder",
        "purpose": "New concept: grow and trim collections with `List<T>`.",
        "concept": "List operations",
        "syntax": "var supplies = new List<string>();",
        "docs": "https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1",
        "story": (
            "The swamp snack bar only accepts orders tracked in a flexible list—otherwise the chef pelican refuses to cook."
        ),
        "task": (
            "Start a `List<string>` with one supply, add another, remove the first, then loop through the remaining items and print them."
        ),
        "example": "Output\nStill packed: extra socks",
        "solution": "var supplies = new System.Collections.Generic.List<string> { \"hot sauce\" };\nsupplies.Add(\"extra socks\");\nsupplies.Remove(\"hot sauce\");\nforeach (var item in supplies)\n{\n    Console.WriteLine($\"Still packed: {item}\");\n}",
    },
    {
        "number": "28",
        "slug": "dictionary-dossier",
        "purpose": "New concept: map keys to values with `Dictionary<TKey, TValue>`.",
        "concept": "Dictionary lookup",
        "syntax": "var map = new Dictionary<string, int>();",
        "docs": "https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2",
        "story": (
            "Checkpoint mimics only unlock when John proves he can pair each biome with its guard count."
        ),
        "task": (
            "Create a `Dictionary<string, int>` with two biome entries. Print a formatted message that includes one biome's guard count using the dictionary lookup."
        ),
        "example": "Output\nLabyrinth employs 4 guards.",
        "solution": "var guardRoster = new System.Collections.Generic.Dictionary<string, int>\n{\n    [\"Labyrinth\"] = 4,\n    [\"Sarcastic Swamp\"] = 6\n};\nConsole.WriteLine($\"Labyrinth employs {guardRoster[\"Labyrinth\"]} guards.\");",
    },
    {
        "number": "29",
        "slug": "enum-ensemble",
        "purpose": "New concept: model named constants with an `enum`.",
        "concept": "Enum declaration",
        "syntax": "enum BiomeMood { Calm, Curious, Snarky }",
        "docs": "https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/enum",
        "story": (
            "A mood crystal hums only when presented with an official enum of swamp temperaments."
        ),
        "task": (
            "Declare an enum listing three moods and print one of the values."
        ),
        "example": "Output\nCurrent mood: Curious",
        "solution": "Console.WriteLine($\"Current mood: {BiomeMood.Curious}\");\n\nenum BiomeMood\n{\n    Calm,\n    Curious,\n    Snarky\n}",
    },
    {
        "number": "30",
        "slug": "enum-translator",
        "purpose": "New concept: convert enums to and from strings/ints.",
        "concept": "Enum conversion",
        "syntax": "Enum.Parse<BiomeMood>(\"Snarky\");",
        "docs": "https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/enum#conversions",
        "story": (
            "A bureaucratic eel demands mood paperwork in every format—numeric, text, and enum."
        ),
        "task": (
            "Pick an enum value, cast it to `int`, parse a string back to the enum, then print both results."
        ),
        "example": "Output\nNumeric mood: 1\nParsed mood: Snarky",
        "solution": "BiomeMood mood = BiomeMood.Curious;\nint numeric = (int)mood;\nBiomeMood parsed = Enum.Parse<BiomeMood>(\"Snarky\");\nConsole.WriteLine($\"Numeric mood: {numeric}\");\nConsole.WriteLine($\"Parsed mood: {parsed}\");\n\nenum BiomeMood\n{\n    Calm = 0,\n    Curious = 1,\n    Snarky = 2\n}",
    },
    {
        "number": "31",
        "slug": "flag-festival",
        "purpose": "New concept: combine enum flags with bitwise OR.",
        "concept": "[Flags] enum",
        "syntax": "LabGear pack = LabGear.Map | LabGear.Lantern;",
        "docs": "https://learn.microsoft.com/dotnet/api/system.flagsattribute",
        "story": (
            "Festival ushers only admit adventurers who pack multiple gear flags and can read them back with pride."
        ),
        "task": (
            "Create a `[Flags]` enum for gear items, combine two flags, and print the composite pack."
        ),
        "example": "Output\nPack includes: Lantern, Boots",
        "solution": "LabGear pack = LabGear.Lantern | LabGear.Boots;\nConsole.WriteLine($\"Pack includes: {pack}\");\n\n[Flags]\nenum LabGear\n{\n    None = 0,\n    Lantern = 1,\n    Map = 2,\n    Boots = 4\n}",
    },
    {
        "number": "32",
        "slug": "interface-pact",
        "purpose": "New concept: declare an interface to describe a contract.",
        "concept": "Interface definition",
        "syntax": "interface IChant { string Sing(); }",
        "docs": "https://learn.microsoft.com/dotnet/csharp/programming-guide/interfaces/",
        "story": (
            "A labyrinth attorney demands a formal chant contract before approving soundtrack requests."
        ),
        "task": (
            "Define an interface with one method and a class that implements it. Create the class and call the interface method, printing the result."
        ),
        "example": "Output\nChant: Echoing wifi lullaby",
        "solution": "IChant bard = new Bard();\nConsole.WriteLine($\"Chant: {bard.Sing()}\");\n\ninterface IChant\n{\n    string Sing();\n}\n\nclass Bard : IChant\n{\n    public string Sing() => \"Echoing wifi lullaby\";\n}",
    },
    {
        "number": "33",
        "slug": "multi-interface-mixer",
        "purpose": "New concept: implement multiple interfaces on one class.",
        "concept": "Multiple interfaces",
        "syntax": "class Mimic : IChant, IAlarm",
        "docs": "https://learn.microsoft.com/dotnet/csharp/programming-guide/interfaces/explicit-interface-implementation",
        "story": (
            "A shape-shifting mimic offers contracts only if John can juggle several interface obligations at once."
        ),
        "task": (
            "Create two interfaces with different methods and a class implementing both. Use each interface reference to call its respective method and print the messages."
        ),
        "example": "Output\nReport: Mood stable\nAlarm: Confetti deployed",
        "solution": "IMoodReporter reporter = new MimicChest();\nIAlarmRaiser alarm = new MimicChest();\nConsole.WriteLine($\"Report: {reporter.Describe()}\");\nConsole.WriteLine($\"Alarm: {alarm.Trigger()}\");\n\ninterface IMoodReporter\n{\n    string Describe();\n}\n\ninterface IAlarmRaiser\n{\n    string Trigger();\n}\n\nclass MimicChest : IMoodReporter, IAlarmRaiser\n{\n    public string Describe() => \"Mood stable\";\n    public string Trigger() => \"Confetti deployed\";\n}",
    },
    {
        "number": "34",
        "slug": "polymorph-play",
        "purpose": "New concept: invoke polymorphic behavior through interface references.",
        "concept": "Polymorphism",
        "syntax": "foreach (var actor in troupe) actor.Perform();",
        "docs": "https://learn.microsoft.com/dotnet/csharp/fundamentals/object-oriented/polymorphism",
        "story": (
            "An undersea improv troupe only performs when the audience can treat every actor as the same contract while letting each improvise wildly."
        ),
        "task": (
            "Populate a list of performers implementing the same interface. Loop over the list calling the shared method, printing each unique result."
        ),
        "example": "Output\nPerformance: Bard strums wifi blues\nPerformance: Goblin beatboxes bug fixes",
        "solution": "var performers = new System.Collections.Generic.List<IPerformer>\n{\n    new BardPerformer(),\n    new GoblinPerformer()\n};\n\nforeach (var performer in performers)\n{\n    Console.WriteLine($\"Performance: {performer.Perform()}\");\n}\n\ninterface IPerformer\n{\n    string Perform();\n}\n\nclass BardPerformer : IPerformer\n{\n    public string Perform() => \"Bard strums wifi blues\";\n}\n\nclass GoblinPerformer : IPerformer\n{\n    public string Perform() => \"Goblin beatboxes bug fixes\";\n}\n",
    },
    {
        "number": "35",
        "slug": "try-guardian",
        "purpose": "New concept: catch exceptions with `try`/`catch`.",
        "concept": "try/catch",
        "syntax": "try { ... } catch (FormatException) { ... }",
        "docs": "https://learn.microsoft.com/dotnet/csharp/language-reference/statements/exception-handling-statements",
        "story": (
            "An annoyed swamp accountant tosses random scroll inputs. John must guard against bad formats gracefully."
        ),
        "task": (
            "Wrap an `int.Parse` call in a `try/catch`. Print a success message or a fallback line when parsing fails."
        ),
        "example": "Output\nParse failed: invalid rune number.",
        "solution": "try\n{\n    int id = int.Parse(\"not-a-number\");\n    Console.WriteLine($\"Parsed rune: {id}\");\n}\ncatch (FormatException)\n{\n    Console.WriteLine(\"Parse failed: invalid rune number.\");\n}",
    },
    {
        "number": "36",
        "slug": "catch-hierarchy",
        "purpose": "New concept: order specific catches before general ones.",
        "concept": "Catch ordering",
        "syntax": "catch (InvalidOperationException) { } catch (Exception) { }",
        "docs": "https://learn.microsoft.com/dotnet/csharp/fundamentals/exceptions/",
        "story": (
            "A sarcastic vine tests whether John handles precise grievances before generic grumbles."
        ),
        "task": (
            "Throw an `InvalidOperationException` inside a `try` block, catch it specifically, then fall back to a general `Exception` catch that would run otherwise. Print which catch triggered."
        ),
        "example": "Output\nHandled specific swamp hiccup.",
        "solution": "try\n{\n    ThrowSwampError();\n}\ncatch (InvalidOperationException)\n{\n    Console.WriteLine(\"Handled specific swamp hiccup.\");\n}\ncatch (Exception)\n{\n    Console.WriteLine(\"Handled generic issue.\");\n}\n\nstatic void ThrowSwampError()\n{\n    throw new InvalidOperationException(\"Mud refused to stay put.\");\n}",
    },
    {
        "number": "37",
        "slug": "using-safeguard",
        "purpose": "New concept: ensure cleanup with the `using` statement.",
        "concept": "using statement",
        "syntax": "using var reader = new StringReader(...);",
        "docs": "https://learn.microsoft.com/dotnet/csharp/language-reference/statements/using",
        "story": (
            "A librarian mermaid hands out soggy parchment but requires proof that John disposes of magical readers responsibly."
        ),
        "task": (
            "Use a `using` declaration with `StringReader` to consume two lines of text and print them."
        ),
        "example": "Output\nFirst line: Labyrinth logs\nSecond line: Swamp minutes",
        "solution": "using var reader = new System.IO.StringReader(\"Labyrinth logs\\nSwamp minutes\");\nConsole.WriteLine($\"First line: {reader.ReadLine()}\");\nConsole.WriteLine($\"Second line: {reader.ReadLine()}\");",
    },
    {
        "number": "38",
        "slug": "linq-scout",
        "purpose": "New concept: filter sequences with LINQ `Where`.",
        "concept": "LINQ Where",
        "syntax": "var calmRooms = rooms.Where(r => r.Contains(\"Calm\"));",
        "docs": "https://learn.microsoft.com/dotnet/csharp/programming-guide/concepts/linq/",
        "story": (
            "A scoutfish only relays calm meeting rooms if John filters the full reef schedule with fluent LINQ magic."
        ),
        "task": (
            "Create an array of room names and use `Where` to keep only those containing the word `Calm`. Iterate the filtered results and print each one."
        ),
        "example": "Output\nCalm Coral Council",
        "solution": "var rooms = new[] { \"Calm Coral Council\", \"Noisy Eel Briefing\", \"Calm Bubble Pod\" };\nvar calmRooms = System.Linq.Enumerable.Where(rooms, room => room.Contains(\"Calm\"));\nforeach (var room in calmRooms)\n{\n    Console.WriteLine(room);\n}",
    },
    {
        "number": "39",
        "slug": "linq-transform",
        "purpose": "New concept: project data with LINQ `Select`.",
        "concept": "LINQ Select",
        "syntax": "var chants = beats.Select(b => $\"Beat {b}\");",
        "docs": "https://learn.microsoft.com/dotnet/api/system.linq.enumerable.select",
        "story": (
            "A rhythm octopus wants every beat turned into a chant string using LINQ instead of manual loops."
        ),
        "task": (
            "Start with an integer array of beat numbers. Use `Select` to create strings like `Beat 1 ready`. Print each transformed chant."
        ),
        "example": "Output\nBeat 1 ready\nBeat 2 ready\nBeat 3 ready",
        "solution": "var beats = new[] { 1, 2, 3 };\nvar chants = System.Linq.Enumerable.Select(beats, beat => $\"Beat {beat} ready\");\nforeach (var chant in chants)\n{\n    Console.WriteLine(chant);\n}",
    },
    {
        "number": "40",
        "slug": "linq-ledger",
        "purpose": "New concept: order and aggregate with LINQ `OrderBy` and `Sum`.",
        "concept": "LINQ OrderBy + Sum",
        "syntax": "int total = loot.OrderBy(x => x).Sum();",
        "docs": "https://learn.microsoft.com/dotnet/api/system.linq.enumerable.orderby",
        "story": (
            "The ledger kraken insists that loot is sorted and tallied in elegant fluent style."
        ),
        "task": (
            "Create an array of treasure values, order them ascending, compute the sum, and print both the sorted list and total."
        ),
        "example": "Output\nSorted loot: 1, 3, 5\nTotal sparkle: 9",
        "solution": "var loot = new[] { 5, 1, 3 };\nvar sorted = System.Linq.Enumerable.OrderBy(loot, value => value).ToArray();\nint total = System.Linq.Enumerable.Sum(sorted);\nConsole.WriteLine($\"Sorted loot: {string.Join(\", \", sorted)}\");\nConsole.WriteLine($\"Total sparkle: {total}\");",
    },
    {
        "number": "41",
        "slug": "file-scroll",
        "purpose": "New concept: read all lines from a text file with `File.ReadAllLines`.",
        "concept": "File.ReadAllLines",
        "syntax": "var lines = File.ReadAllLines(path);",
        "docs": "https://learn.microsoft.com/dotnet/api/system.io.file.readalllines",
        "story": (
            "The archive turtle only hands over the next clue if John proves he can read a scroll file end-to-end."
        ),
        "task": (
            "Write two lines of text to a file, then use `File.ReadAllLines` to load them and print each line with context."
        ),
        "example": "Output\nLine 1: Labyrinth memo\nLine 2: Swamp memo",
        "solution": "var path = \"scroll.txt\";\nSystem.IO.File.WriteAllText(path, \"Labyrinth memo\\nSwamp memo\");\nstring[] lines = System.IO.File.ReadAllLines(path);\nConsole.WriteLine($\"Line 1: {lines[0]}\");\nConsole.WriteLine($\"Line 2: {lines[1]}\");",
    },
    {
        "number": "42",
        "slug": "json-message",
        "purpose": "New concept: serialize data with `JsonSerializer`.",
        "concept": "JSON serialize",
        "syntax": "JsonSerializer.Serialize(data);",
        "docs": "https://learn.microsoft.com/dotnet/standard/serialization/system-text-json-overview",
        "story": (
            "A bureaucratic crab requires that meeting notes be packaged as JSON before stamping them with approval."
        ),
        "task": (
            "Create a simple class with two properties, instantiate it, serialize it to JSON, and print the JSON string."
        ),
        "example": "Output\n{\"Hero\":\"John\",\"Status\":\"Prepared\"}",
        "solution": "var report = new MeetingReport { Hero = \"John\", Status = \"Prepared\" };\nstring json = System.Text.Json.JsonSerializer.Serialize(report);\nConsole.WriteLine(json);\n\nclass MeetingReport\n{\n    public string Hero { get; set; } = string.Empty;\n    public string Status { get; set; } = string.Empty;\n}",
    },
    {
        "number": "43",
        "slug": "file-copy-ritual",
        "purpose": "New concept: write text with a `using` wrapped `StreamWriter`.",
        "concept": "StreamWriter with using",
        "syntax": "using var writer = new StreamWriter(path);",
        "docs": "https://learn.microsoft.com/dotnet/api/system.io.streamwriter",
        "story": (
            "The gratitude goblin only bows when thank-you notes are penned inside a proper `using` ritual."
        ),
        "task": (
            "Use a `StreamWriter` inside a `using` declaration to write a thank-you line to a file, then read the file back and print it."
        ),
        "example": "Output\nStored thanks: Thanks, labyrinth janitor!",
        "solution": "var path = \"thanks.txt\";\nusing (var writer = new System.IO.StreamWriter(path))\n{\n    writer.WriteLine(\"Thanks, labyrinth janitor!\");\n}\nConsole.WriteLine($\"Stored thanks: {System.IO.File.ReadAllText(path).Trim()}\");",
    },
    {
        "number": "44",
        "slug": "delegate-drum",
        "purpose": "New concept: declare and invoke a custom delegate type.",
        "concept": "Custom delegate",
        "syntax": "public delegate string Chant(string name);",
        "docs": "https://learn.microsoft.com/dotnet/csharp/programming-guide/delegates/",
        "story": (
            "A rune drum only responds when a delegate is declared to route chants precisely through its echo chambers."
        ),
        "task": (
            "Declare a delegate that takes a string and returns a string. Instantiate it with a lambda that formats a chant, then invoke and print the result."
        ),
        "example": "Output\nChanting: Rise, Debugsworth!",
        "solution": "Chant caster = name => $\"Rise, {name}!\";\nConsole.WriteLine($\"Chanting: {caster(\"Debugsworth\")}\");\n\ndelegate string Chant(string name);",
    },
    {
        "number": "45",
        "slug": "lambda-light",
        "purpose": "New concept: use built-in `Action` and `Func` with lambdas.",
        "concept": "Action & Func",
        "syntax": "Action wave = () => ...;",
        "docs": "https://learn.microsoft.com/dotnet/api/system.action",
        "story": (
            "Crystal spotlights only track heroes who choreograph lambdas for both actions and calculations."
        ),
        "task": (
            "Create an `Action` that prints a wave and a `Func<int, int>` that doubles sparkles. Invoke both and print their effects."
        ),
        "example": "Output\nWaving to the crowd!\nDoubled sparkles: 8",
        "solution": "Action wave = () => Console.WriteLine(\"Waving to the crowd!\");\nwave();\nFunc<int, int> doubleSparkles = amount => amount * 2;\nConsole.WriteLine($\"Doubled sparkles: {doubleSparkles(4)}\");",
    },
    {
        "number": "46",
        "slug": "event-beacon",
        "purpose": "New concept: raise and subscribe to events.",
        "concept": "Events",
        "syntax": "bell.Rung += handler;",
        "docs": "https://learn.microsoft.com/dotnet/csharp/programming-guide/events/",
        "story": (
            "The guardian bell only rings when heroes wire up proper event handlers to announce the alarm."
        ),
        "task": (
            "Create a class exposing an event. Subscribe with a lambda that prints a message, trigger the event, and ensure the handler fires."
        ),
        "example": "Output\nGuardian bell: alert the swamp crew!",
        "solution": "var bell = new GuardianBell();\nbell.Rung += message => Console.WriteLine($\"Guardian bell: {message}\");\nbell.Ring();\n\nclass GuardianBell\n{\n    public event Action<string>? Rung;\n\n    public void Ring()\n    {\n        Rung?.Invoke(\"alert the swamp crew!\");\n    }\n}",
    },
    {
        "number": "47",
        "slug": "async-scout",
        "purpose": "New concept: craft an `async` method that returns `Task` and awaits work.",
        "concept": "async Task method",
        "syntax": "async Task PingAsync() { await Task.Delay(100); }",
        "docs": "https://learn.microsoft.com/dotnet/csharp/programming-guide/concepts/async/",
        "story": (
            "A sonar dolphin insists on asynchronous pings so the undersea council is never double-booked."
        ),
        "task": (
            "Write an `async` method that awaits `Task.Delay` then prints a confirmation. From top level, await the method so the ping finishes before exiting."
        ),
        "example": "Output\nPreparing ping...\nPing sent!",
        "solution": "await BeaconAsync();\n\nstatic async Task BeaconAsync()\n{\n    Console.WriteLine(\"Preparing ping...\");\n    await Task.Delay(50);\n    Console.WriteLine(\"Ping sent!\");\n}",
    },
    {
        "number": "48",
        "slug": "cancel-signal",
        "purpose": "New concept: respond to a `CancellationToken` in async work.",
        "concept": "CancellationToken",
        "syntax": "token.ThrowIfCancellationRequested();",
        "docs": "https://learn.microsoft.com/dotnet/standard/threading/cancellation",
        "story": (
            "A kelp project manager practices humane meetings: every async scan must halt the moment someone waves the cancel flag."
        ),
        "task": (
            "Create a method that accepts a `CancellationToken`, checks it, and prints whether the scan completed or was canceled. Trigger cancellation before awaiting the task to prove it respects the token."
        ),
        "example": "Output\nScan canceled politely.",
        "solution": "var cts = new System.Threading.CancellationTokenSource();\nvar task = ScanAsync(cts.Token);\ncts.Cancel();\ntry\n{\n    await task;\n}\ncatch (OperationCanceledException)\n{\n    Console.WriteLine(\"Scan canceled politely.\");\n}\n\nstatic async Task ScanAsync(System.Threading.CancellationToken token)\n{\n    token.ThrowIfCancellationRequested();\n    await Task.Delay(10, token);\n    Console.WriteLine(\"Scan completed.\");\n}",
    }
]
