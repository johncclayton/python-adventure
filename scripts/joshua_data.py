EXERCISES = [
    {
        "number": "01",
        "slug": "court-horn",
        "purpose": "New concept: print lines with `print()` to wake the practice arena.",
        "concept": "Print text",
        "syntax": "print(\"Swish!\")",
        "docs": "https://docs.python.org/3/library/functions.html#print",
        "story": (
            "Coach Flexadecimal rigged the gym lights to activate only when the court hears a two-line chant about hoops and protein."
        ),
        "task": (
            "Write a script that prints two hype lines, each mentioning a different snack that fuels practice."
        ),
        "example": "Output\nSwish the spinach smoothie!\nBank the black-bean burrito!",
        "solution": "print(\"Swish the spinach smoothie!\")\nprint(\"Bank the black-bean burrito!\")",
    },
    {
        "number": "02",
        "slug": "repl-echo-siren",
        "purpose": "New concept: capture input with `input()` and echo it back.",
        "concept": "Read input",
        "syntax": "chant = input(\"Chant: \")",
        "docs": "https://docs.python.org/3/library/functions.html#input",
        "story": (
            "A grumpy gym speaker refuses to blast today's rally until it hears Joshua repeat whatever chant he whispers into the REPL."
        ),
        "task": (
            "Ask the user for a rally chant, then print a sentence announcing that chant is blasting across the arena."
        ),
        "example": "Input\nTofu Alley-Oop\nOutput\nRebroadcasting: Tofu Alley-Oop!",
        "solution": (
            "chant = input(\"Declare your rally: \")\n"
            "print(\"Rebroadcasting: \" + chant + \"!\")"
        ),
    },
    {
        "number": "03",
        "slug": "stat-sheet-scribes",
        "purpose": "New concept: assign numbers, strings, and booleans to variables.",
        "concept": "Store values in variables",
        "syntax": "shots_made = 5",
        "docs": "https://docs.python.org/3/reference/simple_stmts.html#assignment-statements",
        "story": (
            "The locker room clipboard has blank spots for Joshua's name, shot total, and whether stretching is done. It only unlocks if the values are stored neatly."
        ),
        "task": (
            "Create three variables: player name (string), shots made (int), and did stretch (bool). Print each with a label."
        ),
        "example": "Output\nPlayer: Joshua\nShots Made: 4\nStretch Done: True",
        "solution": (
            "player = \"Joshua\"\n"
            "shots_made = 4\n"
            "stretched = True\n\n"
            "print(\"Player:\", player)\n"
            "print(\"Shots Made:\", shots_made)\n"
            "print(\"Stretch Done:\", stretched)"
        ),
    },
    {
        "number": "04",
        "slug": "type-trainer",
        "purpose": "New concept: inspect values with `type()`.",
        "concept": "Use type()",
        "syntax": "type(points)",
        "docs": "https://docs.python.org/3/library/functions.html#type",
        "story": (
            "A protein shaker robot asks Joshua to confirm each stat's type before it mixes the post-game smoothie."
        ),
        "task": (
            "Store a score (int), a favorite shake flavor (string), and the warmup status (bool). Print each value and the result of `type()` for it."
        ),
        "example": "Output\nScore: 18 -> <class 'int'>\nShake: Banana Blitz -> <class 'str'>\nWarmup done: False -> <class 'bool'>",
        "solution": (
            "score = 18\n"
            "flavor = \"Banana Blitz\"\n"
            "warmup_done = False\n\n"
            "print(\"Score:\", score, '->', type(score))\n"
            "print(\"Shake:\", flavor, '->', type(flavor))\n"
            "print(\"Warmup done:\", warmup_done, '->', type(warmup_done))"
        ),
    },
    {
        "number": "05",
        "slug": "scoop-converter",
        "purpose": "New concept: convert text to integers with `int()`.",
        "concept": "Convert to int",
        "syntax": "scoops = int(text)",
        "docs": "https://docs.python.org/3/library/functions.html#int",
        "story": (
            "The nutrition kiosk gathers shout-outs from fans about how many protein scoops to prep tomorrow, but it stores them as strings."
        ),
        "task": (
            "Ask for a scoop count as text, convert it to an int, double it for tomorrow's order, and print the plan."
        ),
        "example": "Input\n3\nOutput\nOrder 6 scoops for tomorrow.",
        "solution": (
            "scoop_text = input(\"How many scoops today? \")\n"
            "scoops = int(scoop_text)\n"
            "print(f\"Order {scoops * 2} scoops for tomorrow.\")"
        ),
    },
    {
        "number": "06",
        "slug": "truth-bench",
        "purpose": "New concept: evaluate truthiness with `bool()`.",
        "concept": "bool() on values",
        "syntax": "bool(value)",
        "docs": "https://docs.python.org/3/library/functions.html#bool",
        "story": (
            "Coach installed a truth bench that tips over if Joshua can't predict which stats count as truthy reps."
        ),
        "task": (
            "Create an empty string, a list with one dumbbell weight, and zero misses. Print each value and its `bool()` result."
        ),
        "example": "Output\nLocker note -> False\nWeight list -> True\nMisses -> False",
        "solution": (
            "locker_note = \"\"\n"
            "weight_list = [135]\n"
            "misses = 0\n\n"
            "print(\"Locker note ->\", bool(locker_note))\n"
            "print(\"Weight list ->\", bool(weight_list))\n"
            "print(\"Misses ->\", bool(misses))"
        ),
    },
    {
        "number": "07",
        "slug": "slice-drill",
        "purpose": "New concept: slice strings to grab substrings.",
        "concept": "String slicing",
        "syntax": "tag[:3]",
        "docs": "https://docs.python.org/3/library/stdtypes.html#common-sequence-operations",
        "story": (
            "A hoop-granting hologram hides the gym code in the first three and last two letters of a protein slogan."
        ),
        "task": (
            "Given a hard-coded slogan string, slice the first three characters and the last two characters, then print both pieces."
        ),
        "example": "Output\nPrefix: GAI\nSuffix: NS",
        "solution": (
            "slogan = \"GAINS AND GRAINS\"\n"
            "prefix = slogan[:3]\n"
            "suffix = slogan[-2:]\n\n"
            "print(\"Prefix:\", prefix)\n"
            "print(\"Suffix:\", suffix)"
        ),
    },
    {
        "number": "08",
        "slug": "fstring-scorebug",
        "purpose": "New concept: format messages with f-strings.",
        "concept": "f-string",
        "syntax": "f\"Score {points}\"",
        "docs": "https://docs.python.org/3/reference/lexical_analysis.html#f-strings",
        "story": (
            "The arena scorebug wants a single string that names Joshua and shows his protein points for the day."
        ),
        "task": (
            "Store Joshua's name and protein points, then print one sentence using an f-string that includes both."
        ),
        "example": "Output\nJoshua logged 24 protein points tonight.",
        "solution": (
            "name = \"Joshua\"\n"
            "protein_points = 24\n"
            "print(f\"{name} logged {protein_points} protein points tonight.\")"
        ),
    },
    {
        "number": "09",
        "slug": "strip-warmup",
        "purpose": "New concept: tidy text with `.strip()`.",
        "concept": "str.strip()",
        "syntax": "chant.strip()",
        "docs": "https://docs.python.org/3/library/stdtypes.html#str.strip",
        "story": (
            "The warmup playlist refuses to load if there are extra spaces before or after the chant name."
        ),
        "task": (
            "Store a chant string with messy spaces on both sides. Use `.strip()` to clean it and print the trimmed chant."
        ),
        "example": "Output\nClean chant: Kale Crushers",
        "solution": (
            "messy = \"   Kale Crushers   \"\n"
            "clean = messy.strip()\n"
            "print(\"Clean chant:\", clean)"
        ),
    },
    {
        "number": "10",
        "slug": "lowercase-layup",
        "purpose": "New concept: normalize text with `.lower()`.",
        "concept": "str.lower()",
        "syntax": "player.lower()",
        "docs": "https://docs.python.org/3/library/stdtypes.html#str.lower",
        "story": (
            "A scouting drone only recognizes players when their names are saved in lowercase to avoid yelling."
        ),
        "task": (
            "Take a mixed-case name and print it in lowercase."
        ),
        "example": "Output\nscouted id: joshua",
        "solution": (
            "name = \"Joshua\"\n"
            "print(\"scouted id:\", name.lower())"
        ),
    },
    {
        "number": "11",
        "slug": "compare-score",
        "purpose": "New concept: compare values with `==` and `!=`.",
        "concept": "Comparison operators",
        "syntax": "shots == goal",
        "docs": "https://docs.python.org/3/library/stdtypes.html#comparisons",
        "story": (
            "The shot-clock goblin checks whether practice goals were hit or missed before opening the smoothie bar."
        ),
        "task": (
            "Store the target shots and actual shots. Print whether Joshua met the goal and whether the score differed using `==` and `!=`."
        ),
        "example": "Output\nGoal met? True\nDifferent than target? False",
        "solution": (
            "target = 20\n"
            "made = 20\n"
            "print(\"Goal met?\", made == target)\n"
            "print(\"Different than target?\", made != target)"
        ),
    },
    {
        "number": "12",
        "slug": "membership-scout",
        "purpose": "New concept: check membership with `in`.",
        "concept": "Membership operator",
        "syntax": "'kale' in snacks",
        "docs": "https://docs.python.org/3/reference/expressions.html#membership-test-operations",
        "story": (
            "The protein pantry door opens when Joshua proves he can spot whether a requested ingredient is already in the stash."
        ),
        "task": (
            "Create a list of available snacks. Use `in` to check if 'kale chips' is stocked and print the result."
        ),
        "example": "Output\nKale chips ready? True",
        "solution": (
            "snacks = ['kale chips', 'peanut butter cups', 'greek yogurt']\n"
            "print(\"Kale chips ready?\", 'kale chips' in snacks)"
        ),
    },
    {
        "number": "13",
        "slug": "logic-huddle",
        "purpose": "New concept: combine booleans with `and`/`or`.",
        "concept": "Logical operators",
        "syntax": "has_ball and has_shoes",
        "docs": "https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not",
        "story": (
            "Coach only starts the scrimmage if Joshua brought both the lucky ball and the extra shoes—or at least the shoes."
        ),
        "task": (
            "Create booleans for owning the lucky ball and carrying spare shoes. Use `and`/`or` to decide if practice can start, then print the verdict."
        ),
        "example": "Output\nPractice cleared? True",
        "solution": (
            "has_ball = False\n"
            "has_shoes = True\n"
            "can_start = has_ball and has_shoes or has_shoes\n"
            "print(\"Practice cleared?\", can_start)"
        ),
    },
    {
        "number": "14",
        "slug": "if-layup",
        "purpose": "New concept: branch with `if`/`else`.",
        "concept": "if/else",
        "syntax": "if shots >= goal: ...",
        "docs": "https://docs.python.org/3/tutorial/controlflow.html#if-statements",
        "story": (
            "The glowing rim flashes green only if Joshua crushed his shot goal; otherwise it offers extra drills."
        ),
        "task": (
            "Store the made shots and goal. Use `if/else` to print either a celebration or a reminder to practice more."
        ),
        "example": "Output\nCelebrate: protein confetti unlocked!",
        "solution": (
            "made = 22\n"
            "goal = 20\n"
            "if made >= goal:\n"
            "    print(\"Celebrate: protein confetti unlocked!\")\n"
            "else:\n"
            "    print(\"More reps: refill the squat rack!\")"
        ),
    },
    {
        "number": "15",
        "slug": "elif-rotation",
        "purpose": "New concept: add extra branches with `elif`.",
        "concept": "elif chain",
        "syntax": "if ... elif ... else ...",
        "docs": "https://docs.python.org/3/tutorial/controlflow.html#if-statements",
        "story": (
            "A sarcastic scoreboard announces different tunes based on hydration levels: dehydrated, okay, or legendary."
        ),
        "task": (
            "Set a hydration percent and use `if/elif/else` to print one of three hydration messages."
        ),
        "example": "Output\nHydration check: legendary cucumber water hero!",
        "solution": (
            "hydration = 95\n"
            "if hydration < 50:\n"
            "    print(\"Hydration check: drink water immediately!\")\n"
            "elif hydration < 90:\n"
            "    print(\"Hydration check: solid but sip more.\")\n"
            "else:\n"
            "    print(\"Hydration check: legendary cucumber water hero!\")"
        ),
    },
    {
        "number": "16",
        "slug": "range-sprints",
        "purpose": "New concept: loop with `for` and `range()`.",
        "concept": "for with range",
        "syntax": "for lap in range(1, 4):",
        "docs": "https://docs.python.org/3/tutorial/controlflow.html#for-statements",
        "story": (
            "The practice floor lights up one lane per sprint as long as Joshua counts them out loud."
        ),
        "task": (
            "Use a `for` loop with `range(1, 4)` to print lap numbers 1 through 3 with a motivational phrase."
        ),
        "example": "Output\nLap 1: glide\nLap 2: sprint\nLap 3: finish strong",
        "solution": (
            "for lap in range(1, 4):\n"
            "    print(f\"Lap {lap}: finish strong\")"
        ),
    },
    {
        "number": "17",
        "slug": "list-lineup",
        "purpose": "New concept: loop through a list with `for`.",
        "concept": "for over list",
        "syntax": "for drill in drills:",
        "docs": "https://docs.python.org/3/tutorial/controlflow.html#for-statements",
        "story": (
            "The assistant coach wants every drill announced before the timer starts."
        ),
        "task": (
            "Create a list of three drills and loop through it, printing `Next drill:` before each name."
        ),
        "example": "Output\nNext drill: crossover ladder\nNext drill: free-throw focus\nNext drill: box-out battle",
        "solution": (
            "drills = ['crossover ladder', 'free-throw focus', 'box-out battle']\n"
            "for drill in drills:\n"
            "    print('Next drill:', drill)"
        ),
    },
    {
        "number": "18",
        "slug": "while-break",
        "purpose": "New concept: manage repetition with `while` and `break`.",
        "concept": "while + break",
        "syntax": "while True: ... break",
        "docs": "https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements",
        "story": (
            "The smoothie fountain keeps pouring samples until the protein meter says stop, so Joshua needs a loop with an escape hatch."
        ),
        "task": (
            "Start a counter at 0. Use a `while True` loop to pour samples, increment the counter, and `break` after three pours. Print each pour number."
        ),
        "example": "Output\nPour 1\nPour 2\nPour 3",
        "solution": (
            "pours = 0\n"
            "while True:\n"
            "    pours += 1\n"
            "    print(f\"Pour {pours}\")\n"
            "    if pours == 3:\n"
            "        break"
        ),
    },
]
