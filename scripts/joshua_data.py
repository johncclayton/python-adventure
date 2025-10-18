EXERCISES = [
    {
        "number": "01",
        "slug": "protein-proclamation",
        "purpose": "Help Joshua run his very first Python file that shouts a pre-game protein war cry.",
        "concept": "Print text to the console",
        "syntax": "print(\"Protein Power! 🏀\")",
        "docs": "https://docs.python.org/3/library/functions.html#print",
        "story": (
            "Coach Flexadecimal just hid the next scouting report inside a blender bottle. "
            "It only pops open if the arena hears a two-line chant about basketball and protein."
        ),
        "task": (
            "Write a script that prints two hype lines, each mentioning a different protein source, so the blender spits out the clue."
        ),
        "example": "Output\nProtein Panthers pump whey for the win!\nEgg-white alley-oops never miss.",
        "solution": "print(\"Protein Panthers pump whey for the win!\")\nprint(\"Egg-white alley-oops never miss.\")",
    },
    {
        "number": "02",
        "slug": "repl-rally-cry",
        "purpose": "Practice grabbing interactive input so Joshua can fist-bump the REPL before every workout.",
        "concept": "Read text from the console",
        "syntax": "name = input(\"Enter chant: \")",
        "docs": "https://docs.python.org/3/library/functions.html#input",
        "story": (
            "A sarcastic chicken is sitting on the next note. It promises to hand it over only if the arena speakers repeat "
            "whatever rally cry Joshua shouts."
        ),
        "task": (
            "Ask the user for a rally cry, then print a sentence announcing that chant is now booming through the arena."
        ),
        "example": "Input\nTofu Thunder Squad\nOutput\nTofu Thunder Squad is now blasting over the speakers!",
        "solution": (
            "rally_cry = input(\"State your rally cry: \")\n"
            "print(rally_cry + \" is now blasting over the speakers!\")"
        ),
    },
    {
        "number": "03",
        "slug": "macro-bench-ledger",
        "purpose": "Teach Joshua to stash stats in variables so he can brag about his gains with evidence.",
        "concept": "Assign values to variables",
        "syntax": "player = \"Joshua\"",
        "docs": "https://docs.python.org/3/reference/simple_stmts.html#assignment-statements",
        "story": (
            "Inside the Broccoli Dunk Bunker, Coach Flexadecimal taped the next clue under a dumbbell. "
            "The chicken guarding it squawks that only players with a neat variable ledger get to lift it."
        ),
        "task": (
            "Create variables for Joshua's name, the number of shakes he chugged today, and whether leg day is complete. "
            "Print each one with a label so the chicken nods respectfully."
        ),
        "example": "Output\nName: Joshua\nShakes Today: 3\nLeg Day Complete: True",
        "solution": (
            "name = \"Joshua\"\n"
            "shakes_today = 3\n"
            "leg_day_complete = True\n\n"
            "print(\"Name:\", name)\n"
            "print(\"Shakes Today:\", shakes_today)\n"
            "print(\"Leg Day Complete:\", leg_day_complete)"
        ),
    },
    {
        "number": "04",
        "slug": "type-taste-test",
        "purpose": "Help Joshua inspect data types before he dumps stats into the mystery blender.",
        "concept": "Inspect a value's type",
        "syntax": "type(points)",
        "docs": "https://docs.python.org/3/library/functions.html#type",
        "story": (
            "The Swolestice Spin Class Coliseum runs on picky machinery. "
            "A holo-chicken refuses to reveal the next hint until Joshua proves he knows which stats are ints, strings, and bools."
        ),
        "task": (
            "Store Joshua's points (int), favorite shake flavor (string), and stretch status (bool). "
            "Print each value alongside the result of calling `type()` on it."
        ),
        "example": "Output\nPoints: 42 -> <class 'int'>\nFlavor: Peanut Butter Blast -> <class 'str'>\nStretched: True -> <class 'bool'>",
        "solution": (
            "points = 42\n"
            "flavor = \"Peanut Butter Blast\"\n"
            "is_stretched = True\n\n"
            "print(\"Points:\", points, '->', type(points))\n"
            "print(\"Flavor:\", flavor, '->', type(flavor))\n"
            "print(\"Stretched:\", is_stretched, '->', type(is_stretched))"
        ),
    },
    {
        "number": "05",
        "slug": "whey-to-int",
        "purpose": "Convert string input into integers so Joshua can tally protein scoops correctly.",
        "concept": "Convert text to integers",
        "syntax": "scoops = int(input_text)",
        "docs": "https://docs.python.org/3/library/functions.html#int",
        "story": (
            "A basket of whey cupcakes hides the coordinates of the next drill. "
            "The guarding rooster agrees to share only if Joshua can convert crowd-reported scoop counts into actual numbers."
        ),
        "task": (
            "Ask the user how many protein scoops they added to the blender. Cast the result to an int, "
            "then print the total scoops doubled to predict tomorrow's order."
        ),
        "example": "Input\n4\nOutput\nTomorrow requires 8 scoops.",
        "solution": (
            "scoops_text = input(\"How many scoops today? \")\n"
            "scoops = int(scoops_text)\n"
            "print(f\"Tomorrow requires {scoops * 2} scoops.\")"
        ),
    },
    {
        "number": "06",
        "slug": "truthy-treadmill",
        "purpose": "Show Joshua how `bool()` judges truthiness so he can predict which stats trigger the trapdoor treadmill.",
        "concept": "Evaluate truthiness with bool()",
        "syntax": "bool(value)",
        "docs": "https://docs.python.org/3/library/functions.html#bool",
        "story": (
            "Coach Flexadecimal installed a trapdoor treadmill under the chickens. "
            "It activates whenever a falsy value arrives. Joshua must test a trio of stats before stepping on it."
        ),
        "task": (
            "Create three variables: an empty string, a list with one dumbbell weight, and zero. "
            "Print each value with `bool(value)` so Joshua knows which ones count as truthy."
        ),
        "example": "Output\nEmpty Chant -> False\nSingle Plate -> True\nZero Hops -> False",
        "solution": (
            "empty_chant = \"\"\n"
            "plate_list = [135]\n"
            "missed_hops = 0\n\n"
            "print(\"Empty Chant ->\", bool(empty_chant))\n"
            "print(\"Single Plate ->\", bool(plate_list))\n"
            "print(\"Zero Hops ->\", bool(missed_hops))"
        ),
    },
    {
        "number": "07",
        "slug": "slice-and-sizzle",
        "purpose": "Practice string slicing to snag the secret code hidden in protein slogans.",
        "concept": "Slice substrings",
        "syntax": "code = slogan[0:3]",
        "docs": "https://docs.python.org/3/library/stdtypes.html#common-sequence-operations",
        "story": (
            "A hen bench-pressing kale shakes carved a message into a protein bar. "
            "The first three letters unlock the next clue, but the rest is just sticky caramel."
        ),
        "task": (
            "Given a hard-coded slogan string, slice out the first three letters and the last two letters. "
            "Print both pieces so Joshua can stitch together the arena password."
        ),
        "example": "Output\nPrefix: PRO\nSuffix: IN",
        "solution": (
            "slogan = \"PROTEIN PARADE\"\n"
            "prefix = slogan[0:3]\n"
            "suffix = slogan[-2:]\n\n"
            "print(\"Prefix:\", prefix)\n"
            "print(\"Suffix:\", suffix)"
        ),
    },
    {
        "number": "08",
        "slug": "fstring-flex",
        "purpose": "Introduce f-strings so Joshua can brag with extremely specific protein stats.",
        "concept": "Format strings with f-strings",
        "syntax": "f\"score {points}\"",
        "docs": "https://docs.python.org/3/reference/lexical_analysis.html#f-strings",
        "story": (
            "The Zero-Gravity Smoothie Nebula projection keeps roasting Joshua's math. "
            "It wants a perfectly formatted bragging sentence combining his points and shake flavor."
        ),
        "task": (
            "Create variables for total points and shake flavor. Use an f-string to print a single sentence that includes both stats "
            "and mentions the clue hidden in the cup holder."
        ),
        "example": "Output\nJoshua scored 31 points while sipping Strawberry Squat Fuel to earn the hidden clue.",
        "solution": (
            "points = 31\n"
            "flavor = \"Strawberry Squat Fuel\"\n"
            "print(f\"Joshua scored {points} points while sipping {flavor} to earn the hidden clue.\")"
        ),
    },
    {
        "number": "09",
        "slug": "strip-chalk-scrub",
        "purpose": "Use `.strip()` to clean crowd input before the protein chalkboard records it.",
        "concept": "Remove leading and trailing whitespace",
        "syntax": "clean = raw.strip()",
        "docs": "https://docs.python.org/3/library/stdtypes.html#str.strip",
        "story": (
            "The arena chalkboard is coated in protein powder dust. "
            "A prankster chicken entered the next clue with messy spaces, so Joshua has to tidy it before the board accepts it."
        ),
        "task": (
            "Start with a string that has leading and trailing spaces plus a newline. Use `.strip()` to clean it, then print the cleaned result "
            "inside angle brackets so everyone sees it's tidy."
        ),
        "example": "Output\n<Broccoli Dunk Bunker>",
        "solution": (
            "raw_clue = \"  Broccoli Dunk Bunker \n\"\n"
            "clean_clue = raw_clue.strip()\n"
            "print(f\"<{clean_clue}>\")"
        ),
    },
    {
        "number": "10",
        "slug": "lowercase-locker",
        "purpose": "Teach Joshua to normalize text with `.lower()` so locker codes stop failing.",
        "concept": "Convert text to lowercase",
        "syntax": "code.lower()",
        "docs": "https://docs.python.org/3/library/stdtypes.html#str.lower",
        "story": (
            "Coach Flexadecimal hid the next dossier in a locker labelled by rebellious chickens. "
            "The scanner only accepts lowercase codes, even if the crowd yells in uppercase."
        ),
        "task": (
            "Take a mixed-case password string and print its lowercase version with a confirming sentence. "
            "This proves Joshua can normalize any future locker clue."
        ),
        "example": "Output\nThe locker now recognizes code: crunchmasters unite",
        "solution": (
            "password = \"CrunchMasters Unite\"\n"
            "lowered = password.lower()\n"
            "print(f\"The locker now recognizes code: {lowered}\")"
        ),
    },
]
